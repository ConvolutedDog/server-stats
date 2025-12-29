#!/usr/bin/env python3
"""
SSH Audit Dashboard Generator
- Read ssh_login_minutes.csv file
- Process data and generate interactive dashboard
- Output to dashboard/index.html
"""

import pandas as pd
import json
import os
from collections import defaultdict
from datetime import datetime


class DashboardGenerator:
    """SSH Audit Dashboard Generator"""

    def __init__(self, csv_path):
        """Initialize generator with CSV file path"""
        self.csv_path = csv_path

    def process_data(self):
        """Process CSV data and prepare for visualization"""
        try:
            # Read and clean CSV data
            df = pd.read_csv(self.csv_path)
            df["date"] = pd.to_datetime(df["date"])
            df = df.sort_values("date")

            # Extract user names (all columns except date)
            users = [col for col in df.columns if col != "date"]

            # Convert minutes to hours and clean data
            for user in users:
                df[user] = pd.to_numeric(df[user], errors="coerce").fillna(0)
                df[user] = (df[user] / 60).round(2)

            # --- 1. Trend Chart Data ---
            # Daily data (all data, will be filtered by month in frontend)
            df_daily = df.copy()
            daily_labels = df_daily["date"].dt.strftime("%Y-%m-%d").tolist()

            # Monthly data (aggregated)
            df["month"] = df["date"].dt.strftime("%Y-%m")
            df_monthly = df.groupby("month")[users].sum().reset_index()
            monthly_labels = df_monthly["month"].tolist()

            # --- 2. Pie Chart Data ---
            # A. Overall distribution (all time)
            total_sums = df[users].sum().sort_values(ascending=False)
            pie_total_labels = total_sums.index.tolist()
            pie_total_data = total_sums.values.tolist()

            # B. Monthly distribution (split by month)
            # Structure: {"2025-04": {"labels": [u1, u2], "data": [100, 20]}, ...}
            monthly_pie_data = {}
            available_months = df_monthly["month"].tolist()

            for _, row in df_monthly.iterrows():
                month = row["month"]
                # Filter out users with zero data for this month to avoid too many zero values in pie chart
                row_data = row[users]
                valid_data = row_data[row_data > 0].sort_values(ascending=False)

                monthly_pie_data[month] = {
                    "labels": valid_data.index.tolist(),
                    "data": valid_data.values.tolist(),
                }

            # --- 3. Generate Color Configuration ---
            # Extended color palette for multiple users
            base_colors = [
                "#3b82f6",
                "#ef4444",
                "#10b981",
                "#f59e0b",
                "#8b5cf6",
                "#ec4899",
                "#6366f1",
                "#14b8a6",
                "#f97316",
                "#06b6d4",
                "#84cc16",
                "#a855f7",
                "#d946ef",
                "#f43f5e",
                "#64748b",
                "#9ca3af",
                "#cbd5e1",
                "#475569",
                "#334155",
                "#1e293b",
            ]

            # Ensure each user has a fixed color mapping
            user_color_map = {
                user: base_colors[i % len(base_colors)] for i, user in enumerate(users)
            }

            # Build Chart.js datasets (for trend charts)
            def build_datasets(source_df, label_col):
                datasets = []
                for user in users:
                    datasets.append(
                        {
                            "label": user,
                            "data": source_df[user].tolist(),
                            "borderColor": user_color_map[user],
                            "backgroundColor": user_color_map[
                                user
                            ],  # For bar/pie charts
                            "borderWidth": 2,
                            "tension": 0.3,
                            "pointRadius": 2,
                            "fill": False,
                        }
                    )
                return datasets

            # Prepare all daily and monthly data
            daily_all_data = {
                "labels": daily_labels,
                "datasets": build_datasets(df_daily, "date"),
            }
            monthly_all_data = {
                "labels": monthly_labels,
                "datasets": build_datasets(df_monthly, "month"),
            }

            return {
                "daily_all": daily_all_data,  # All daily data
                "monthly_all": monthly_all_data,  # All monthly data
                "pie_total": {
                    "labels": pie_total_labels,
                    "data": pie_total_data,
                    "backgroundColor": [user_color_map[u] for u in pie_total_labels],
                },
                "pie_monthly_raw": monthly_pie_data,  # Raw dictionary for frontend processing
                "user_colors": user_color_map,  # Color mapping passed to frontend
                "months_list": available_months,  # For dropdown generation
                "stats": {
                    "total_hours": f"{df[users].sum().sum():,.1f}",
                    "user_count": len(users),
                    "last_update": df["date"].max().strftime("%Y-%m-%d"),
                },
                "ranking": [
                    {"rank": i + 1, "user": u, "hours": f"{v:.1f}"}
                    for i, (u, v) in enumerate(total_sums.items())
                ],
                "date_range": {
                    "first_date": df["date"].min().strftime("%Y-%m-%d"),
                    "last_date": df["date"].max().strftime("%Y-%m-%d"),
                    "first_month": (
                        df_monthly["month"].iloc[0] if len(df_monthly) > 0 else ""
                    ),
                    "last_month": (
                        df_monthly["month"].iloc[-1] if len(df_monthly) > 0 else ""
                    ),
                },
            }

        except Exception as e:
            print(f"❌ Error processing data: {e}")
            import traceback

            traceback.print_exc()
            return None

    def generate_html(self, data):
        """Generate HTML dashboard with processed data"""

        # Generate month selector options
        months_options = ""
        for month in data["months_list"]:
            months_options += f'<option value="{month}">{month}</option>'

        # Generate year selector options
        years = sorted(
            set([m.split("-")[0] for m in data["months_list"]]), reverse=True
        )
        years_options = ""
        for year in years:
            years_options += f'<option value="{year}">{year}</option>'

        html_content = f"""
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SSH 审计看板 Pro</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-zoom@2.0.1/dist/chartjs-plugin-zoom.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <style>
        :root {{
            --bg-dark: #0f172a;
            --card-bg: #1e293b;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --accent: #3b82f6;
            --accent-light: #60a5fa;
            --border: #334155;
            --success: #10b981;
            --danger: #ef4444;
            --warning: #f59e0b;
        }}

        body {{
            background-color: var(--bg-dark);
            color: var(--text-main);
            font-family: 'Segoe UI', Roboto, -apple-system, BlinkMacSystemFont, sans-serif;
            margin: 0; padding: 20px;
        }}

        .container {{ 
            max-width: 1400px; 
            margin: 0 auto; 
        }}

        /* 标题区域样式 */
        .header-section {{
            margin-bottom: 30px;
            position: relative;
        }}

        .header-main {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 20px;
            margin-bottom: 10px;
        }}

        .title-container {{
            flex: 1;
            min-width: 300px;
        }}

        .main-title {{
            margin: 0;
            font-size: 28px;
            font-weight: 700;
            background: linear-gradient(135deg, var(--accent) 0%, var(--accent-light) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            display: flex;
            align-items: center;
            gap: 12px;
        }}

        .title-icon {{
            font-size: 24px;
            background: rgba(59, 130, 246, 0.15);
            padding: 10px;
            border-radius: 12px;
            color: var(--accent);
        }}

        .title-subtext {{
            color: var(--text-muted);
            font-size: 13px;
            margin-top: 6px;
            letter-spacing: 0.5px;
            opacity: 0.9;
        }}

        .header-info {{
            display: flex;
            gap: 15px;
            flex-wrap: wrap;
        }}

        .info-card {{
            display: flex;
            align-items: center;
            gap: 12px;
            background: rgba(30, 41, 59, 0.7);
            padding: 12px 18px;
            border-radius: 12px;
            border: 1px solid rgba(59, 130, 246, 0.2);
            min-width: 180px;
            transition: all 0.3s ease;
        }}

        .info-card:hover {{
            background: rgba(30, 41, 59, 0.9);
            border-color: rgba(59, 130, 246, 0.4);
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
        }}

        .info-icon {{
            font-size: 16px;
            color: var(--accent);
            background: rgba(59, 130, 246, 0.1);
            padding: 8px;
            border-radius: 10px;
            width: 32px;
            height: 32px;
            display: flex;
            align-items: center;
            justify-content: center;
        }}

        .info-content {{
            display: flex;
            flex-direction: column;
        }}

        .info-label {{
            color: var(--text-muted);
            font-size: 11px;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            opacity: 0.8;
        }}

        .info-value {{
            color: var(--text-main);
            font-size: 14px;
            font-weight: 600;
            margin-top: 2px;
        }}

        .header-decoration {{
            position: relative;
            height: 1px;
            background: linear-gradient(90deg, 
                transparent 0%, 
                rgba(59, 130, 246, 0.3) 20%, 
                rgba(59, 130, 246, 0.6) 50%, 
                rgba(59, 130, 246, 0.3) 80%, 
                transparent 100%);
        }}

        .decoration-line {{
            position: absolute;
            top: 0;
            left: 25%;
            right: 25%;
            height: 1px;
            background: linear-gradient(90deg, 
                transparent 0%, 
                rgba(59, 130, 246, 0.8) 50%, 
                transparent 100%);
        }}

        /* 响应式调整 */
        @media (max-width: 768px) {{
            .header-main {{
                flex-direction: column;
                align-items: stretch;
            }}
            
            .title-container {{
                text-align: center;
                min-width: auto;
            }}
            
            .main-title {{
                justify-content: center;
            }}
            
            .header-info {{
                justify-content: center;
            }}
            
            .info-card {{
                min-width: 160px;
                flex: 1;
            }}
        }}

        @media (max-width: 480px) {{
            .header-info {{
                flex-direction: column;
                width: 100%;
            }}
            
            .info-card {{
                width: 100%;
                justify-content: center;
            }}
        }}

        /* 顶部统计卡片 */
        .stats-row {{
            display: grid; 
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px; 
            margin-bottom: 25px;
        }}
        .stat-card {{
            background: var(--card-bg); 
            padding: 20px; 
            border-radius: 12px;
            border: 1px solid var(--border); 
            display: flex; 
            align-items: center; 
            gap: 15px;
        }}
        .stat-icon {{
            width: 45px; 
            height: 45px; 
            background: rgba(59, 130, 246, 0.1);
            border-radius: 10px; 
            display: flex; 
            align-items: center; 
            justify-content: center;
            font-size: 20px; 
            color: var(--accent);
        }}

        /* 图表容器通用样式 */
        .chart-container {{
            background: var(--card-bg); 
            border-radius: 16px; 
            padding: 20px;
            margin-bottom: 25px; 
            border: 1px solid var(--border);
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
        }}
        .chart-header {{
            display: flex; 
            justify-content: space-between; 
            align-items: center;
            margin-bottom: 15px; 
            flex-wrap: wrap; 
            gap: 10px;
        }}
        .chart-header h2 {{ 
            margin: 0; 
            font-size: 16px; 
            color: var(--text-main); 
            display: flex; 
            align-items: center; 
            gap: 8px; 
        }}
        
        /* 月份选择器样式 */
        .month-selector-group {{
            display: flex; 
            align-items: center; 
            gap: 8px; 
            background: #0f172a;
            padding: 4px; 
            border-radius: 8px;
        }}
        .month-selector-group select, .month-selector-group input {{
            background: transparent; 
            border: 1px solid var(--border); 
            color: var(--text-main);
            padding: 5px 10px; 
            border-radius: 6px; 
            font-size: 12px; 
            outline: none;
        }}
        .month-selector-group select:focus, .month-selector-group input:focus {{
            border-color: var(--accent);
        }}
        .month-selector-group .month-label {{
            font-size: 11px; 
            color: var(--text-muted); 
            white-space: nowrap;
        }}
        .apply-btn {{
            background: var(--accent); 
            color: white; 
            border: none; 
            padding: 5px 10px;
            border-radius: 6px; 
            cursor: pointer; 
            font-size: 11px; 
            transition: opacity 0.2s;
        }}
        .apply-btn:hover {{ 
            opacity: 0.9; 
        }}
        
        /* 按钮组 */
        .chart-controls {{ 
            display: flex; 
            gap: 5px; 
            background: #0f172a; 
            padding: 4px; 
            border-radius: 8px; 
        }}
        .chart-controls button, .chart-controls select {{
            background: transparent; 
            border: none; 
            color: var(--text-muted);
            padding: 5px 10px; 
            border-radius: 6px; 
            cursor: pointer; 
            font-size: 12px;
            display: flex; 
            align-items: center; 
            gap: 5px; 
            transition: all 0.2s;
        }}
        .chart-controls button:hover {{ 
            color: var(--text-main); 
            background: rgba(255,255,255,0.05); 
        }}
        .chart-controls button.active {{ 
            background: var(--accent); 
            color: white; 
        }}
        
        /* 特殊按钮颜色 */
        .btn-check:hover {{ 
            color: var(--success) !important; 
        }}
        .btn-trash:hover {{ 
            color: var(--danger) !important; 
        }}
        .btn-reset {{ 
            color: var(--warning) !important; 
        }}
        .btn-reset:hover {{ 
            color: #fbbf24 !important; 
        }}

        /* 下拉框样式 */
        select.custom-select {{
            background: #0f172a; 
            color: var(--text-main); 
            border: 1px solid var(--border);
            padding: 5px 10px; 
            border-radius: 6px; 
            outline: none;
        }}

        /* 饼图区域布局 */
        .pie-grid {{
            display: grid; 
            grid-template-columns: 1fr 1fr; 
            gap: 25px; 
            margin-bottom: 25px;
        }}
        @media (max-width: 768px) {{ 
            .pie-grid {{ 
                grid-template-columns: 1fr; 
            }} 
        }}

        canvas {{ 
            width: 100% !important; 
        }}
        .chart-canvas-wrapper {{ 
            position: relative; 
            height: 350px; 
            width: 100%; 
        }}
        .pie-canvas-wrapper {{ 
            position: relative; 
            height: 300px; 
            width: 100%; 
            display: flex; 
            justify-content: center; 
        }}

    </style>
</head>
<body>

<div class="container">
    <!-- 标题区域 -->
    <div class="header-section">
        <div class="header-main">
            <div class="title-container">
                <h1 class="main-title">
                    <i class="fas fa-shield-alt title-icon"></i>
                    SSH 看板
                </h1>
                <div class="title-subtext">用户登录行为分析与可视化</div>
            </div>
            <div class="header-info">
                <div class="info-card">
                    <i class="fas fa-calendar-alt info-icon"></i>
                    <div class="info-content">
                        <div class="info-label">数据范围</div>
                        <div class="info-value">{data['date_range']['first_date']} - {data['date_range']['last_date']}</div>
                    </div>
                </div>
                <div class="info-card">
                    <i class="fas fa-sync-alt info-icon"></i>
                    <div class="info-content">
                        <div class="info-label">最后更新</div>
                        <div class="info-value">{data['stats']['last_update']}</div>
                    </div>
                </div>
            </div>
        </div>
        <div class="header-decoration">
            <div class="decoration-line"></div>
        </div>
    </div>

    <div class="stats-row">
        <div class="stat-card">
            <div class="stat-icon"><i class="fas fa-clock"></i></div>
            <div>
                <div style="color:var(--text-muted); font-size:12px">所有用户累计登录时长</div>
                <div style="font-weight:bold; font-size:20px">{data['stats']['total_hours']} h</div>
            </div>
        </div>
        <div class="stat-card">
            <div class="stat-icon"><i class="fas fa-users"></i></div>
            <div>
                <div style="color:var(--text-muted); font-size:12px">用户总数</div>
                <div style="font-weight:bold; font-size:20px">{data['stats']['user_count']}</div>
            </div>
        </div>
    </div>

    <div class="pie-grid">
        <div class="chart-container" style="margin-bottom: 0;">
            <div class="chart-header">
                <h2><i class="fas fa-chart-pie"></i> 累计时长占比 (全周期)</h2>
            </div>
            <div class="pie-canvas-wrapper">
                <canvas id="totalPieChart"></canvas>
            </div>
        </div>

        <div class="chart-container" style="margin-bottom: 0;">
            <div class="chart-header">
                <h2><i class="fas fa-calendar-alt"></i> 月度时长占比</h2>
                <div class="chart-controls">
                    <select id="monthSelector" class="custom-select" onchange="updateMonthlyPie()">
                        {months_options}
                    </select>
                </div>
            </div>
            <div class="pie-canvas-wrapper">
                <canvas id="monthlyPieChart"></canvas>
            </div>
        </div>
    </div>

    <div class="chart-container">
        <div class="chart-header">
            <h2><i class="fas fa-chart-line"></i> 月度登录统计趋势</h2>
            <div style="display: flex; gap: 10px;">
                <div class="month-selector-group">
                    <span class="month-label">从:</span>
                    <select id="monthlyStartMonth" style="min-width: 80px;">
                        {months_options}
                    </select>
                    <span class="month-label">到:</span>
                    <select id="monthlyEndMonth" style="min-width: 80px;">
                        {months_options}
                    </select>
                    <button class="apply-btn" onclick="applyMonthRange('monthly')">应用</button>
                </div>
                <div class="chart-controls">
                    <button onclick="toggleAll('monthlyChart', true)" class="btn-check" title="全选">
                        <i class="fas fa-check-double"></i>
                    </button>
                    <button onclick="toggleAll('monthlyChart', false)" class="btn-trash" title="全不选">
                        <i class="fas fa-times"></i>
                    </button>
                    <div style="width: 1px; background: var(--border); margin: 0 5px;"></div>
                    
                    <button onclick="changeType('monthlyChart', 'line')" class="active" id="btn-monthlyChart-line">
                        <i class="fas fa-chart-line"></i>
                    </button>
                    <button onclick="changeType('monthlyChart', 'bar')" id="btn-monthlyChart-bar">
                        <i class="fas fa-chart-bar"></i>
                    </button>
                    <button onclick="toggleStack('monthlyChart')" id="btn-monthlyChart-stack">
                        <i class="fas fa-layer-group"></i>
                    </button>
                    <div style="width: 1px; background: var(--border); margin: 0 5px;"></div>
                    <button onclick="resetZoom('monthlyChart')" class="btn-reset" title="重置缩放">
                        <i class="fas fa-undo-alt"></i>
                    </button>
                </div>
            </div>
        </div>
        <div class="chart-canvas-wrapper">
            <canvas id="monthlyChart"></canvas>
        </div>
    </div>
    
    <div class="chart-container">
        <div class="chart-header">
            <h2><i class="fas fa-calendar-day"></i> 每日登录详情</h2>
            <div style="display: flex; gap: 10px;">
                <div class="month-selector-group">
                    <span class="month-label">从:</span>
                    <select id="dailyStartMonth" style="min-width: 80px;">
                        {months_options}
                    </select>
                    <span class="month-label">到:</span>
                    <select id="dailyEndMonth" style="min-width: 80px;">
                        {months_options}
                    </select>
                    <button class="apply-btn" onclick="applyMonthRange('daily')">应用</button>
                </div>
                <div class="chart-controls">
                    <button onclick="toggleAll('dailyChart', true)" class="btn-check">
                        <i class="fas fa-check-double"></i>
                    </button>
                    <button onclick="toggleAll('dailyChart', false)" class="btn-trash">
                        <i class="fas fa-times"></i>
                    </button>
                    <div style="width: 1px; background: var(--border); margin: 0 5px;"></div>
                    
                    <button onclick="changeType('dailyChart', 'line')" class="active" id="btn-dailyChart-line">
                        <i class="fas fa-chart-line"></i>
                    </button>
                    <button onclick="changeType('dailyChart', 'bar')" id="btn-dailyChart-bar">
                        <i class="fas fa-chart-bar"></i>
                    </button>
                    <div style="width: 1px; background: var(--border); margin: 0 5px;"></div>
                    <button onclick="resetZoom('dailyChart')" class="btn-reset" title="重置缩放">
                        <i class="fas fa-undo-alt"></i>
                    </button>
                </div>
            </div>
        </div>
        <div class="chart-canvas-wrapper">
            <canvas id="dailyChart"></canvas>
        </div>
    </div>

</div>

<script>
    // --- 数据注入 ---
    const rawData = {json.dumps(data)};
    const userColors = rawData.user_colors;
    const monthlyPieData = rawData.pie_monthly_raw;
    
    // --- 全局数据存储 ---
    let allMonthlyData = rawData.monthly_all;
    let allDailyData = rawData.daily_all;
    
    // --- 初始化月份选择器 ---
    function initMonthSelectors() {{
        const months = rawData.months_list;
        if (months.length > 0) {{
            // 设置月度图表：默认显示最近6个月
            const monthlyStartIdx = Math.max(0, months.length - 6);
            document.getElementById('monthlyStartMonth').value = months[monthlyStartIdx];
            document.getElementById('monthlyEndMonth').value = months[months.length - 1];
            
            // 设置日度图表：默认显示最近1个月
            const dailyStartIdx = Math.max(0, months.length - 1);
            document.getElementById('dailyStartMonth').value = months[dailyStartIdx];
            document.getElementById('dailyEndMonth').value = months[months.length - 1];
            
            // 初始化月度饼图选择器为最后一个月
            document.getElementById('monthSelector').value = months[months.length - 1];
        }}
    }}

    // --- Chart.js 全局配置 ---
    Chart.defaults.color = '#94a3b8';
    Chart.defaults.borderColor = '#334155';
    Chart.defaults.font.family = "'Segoe UI', 'Helvetica', 'Arial', sans-serif";
    
    // 通用配置生成器（修改缩放灵敏度）
    function getCommonOptions(isPie = false) {{
        const opts = {{
            responsive: true,
            maintainAspectRatio: false,
            plugins: {{
                legend: {{ 
                    position: isPie ? 'right' : 'bottom', 
                    labels: {{ boxWidth: 12, padding: 15, color: '#cbd5e1' }}
                }},
                // 调整缩放插件配置，降低灵敏度
                zoom: {{
                    pan: {{
                        enabled: true,
                        mode: 'x',
                        modifierKey: 'ctrl',
                    }},
                    zoom: {{
                        wheel: {{
                            enabled: true,
                            speed: 0.1, // 降低滚轮缩放速度
                        }},
                        pinch: {{
                            enabled: true
                        }},
                        mode: 'x',
                    }},
                    limits: {{
                        x: {{ min: 'original', max: 'original' }}
                    }}
                }}
            }}
        }};
        
        if (!isPie) {{
            opts.interaction = {{ mode: 'index', intersect: false }};
            opts.scales = {{
                x: {{ 
                    grid: {{ display: false }},
                    ticks: {{
                        maxRotation: 45,
                        minRotation: 45
                    }}
                }},
                y: {{ 
                    border: {{ display: false }}, 
                    grid: {{ color: '#334155' }},
                    beginAtZero: true
                }}
            }};
        }}
        return opts;
    }}

    // --- 图表实例存储 ---
    const charts = {{}};

    // --- 根据月份范围过滤数据 ---
    function filterDataByMonthRange(dataType, startMonth, endMonth) {{
        const allData = dataType === 'monthly' ? allMonthlyData : allDailyData;
        const labels = allData.labels;
        const datasets = allData.datasets;
        
        if (!labels || labels.length === 0) return {{ labels: [], datasets: [] }};
        
        // 如果是月数据，直接过滤月份
        if (dataType === 'monthly') {{
            const startIdx = labels.indexOf(startMonth);
            const endIdx = labels.indexOf(endMonth);
            
            if (startIdx === -1 || endIdx === -1) return allData;
            
            const filteredLabels = labels.slice(startIdx, endIdx + 1);
            const filteredDatasets = datasets.map(ds => ({{
                ...ds,
                data: ds.data.slice(startIdx, endIdx + 1)
            }}));
            
            return {{ labels: filteredLabels, datasets: filteredDatasets }};
        }}
        // 如果是日数据，需要按日期过滤
        else {{
            const startDate = startMonth + '-01';
            let endDate = endMonth + '-01';
            
            // 计算结束月份的最后一天
            const endMonthDate = new Date(endDate);
            endMonthDate.setMonth(endMonthDate.getMonth() + 1);
            endMonthDate.setDate(0);
            const endDateStr = endMonth + '-' + endMonthDate.getDate().toString().padStart(2, '0');
            
            const startIdx = labels.findIndex(label => label >= startDate);
            const endIdx = labels.findIndex(label => label > endDateStr);
            const actualEndIdx = endIdx === -1 ? labels.length : endIdx;
            
            if (startIdx === -1) return {{ labels: [], datasets: [] }};
            
            const filteredLabels = labels.slice(startIdx, actualEndIdx);
            const filteredDatasets = datasets.map(ds => ({{
                ...ds,
                data: ds.data.slice(startIdx, actualEndIdx)
            }}));
            
            return {{ labels: filteredLabels, datasets: filteredDatasets }};
        }}
    }}

    // --- 初始化趋势图 ---
    function initTrendChart(id, dataType) {{
        const ctx = document.getElementById(id).getContext('2d');
        
        // 获取初始月份范围
        const startMonth = document.getElementById(`${{dataType}}StartMonth`).value;
        const endMonth = document.getElementById(`${{dataType}}EndMonth`).value;
        
        // 过滤数据
        const filteredData = filterDataByMonthRange(dataType, startMonth, endMonth);
        
        charts[id] = new Chart(ctx, {{
            type: 'line',
            data: filteredData,
            options: getCommonOptions(false)
        }});
    }}

    // 初始化图表
    initMonthSelectors();
    initTrendChart('monthlyChart', 'monthly');
    initTrendChart('dailyChart', 'daily');

    // --- 初始化饼图 (总体) ---
    const totalPieCtx = document.getElementById('totalPieChart').getContext('2d');
    new Chart(totalPieCtx, {{
        type: 'doughnut',
        data: {{
            labels: rawData.pie_total.labels,
            datasets: [{{
                data: rawData.pie_total.data,
                backgroundColor: rawData.pie_total.backgroundColor,
                borderWidth: 0,
                hoverOffset: 10
            }}]
        }},
        options: getCommonOptions(true)
    }});

    // --- 初始化饼图 (月度 - 动态) ---
    let monthlyPieChart = null;
    
    function updateMonthlyPie() {{
        const selector = document.getElementById('monthSelector');
        const selectedMonth = selector.value;
        const currentData = monthlyPieData[selectedMonth];
        
        if (!currentData) {{
            console.warn(`No data for month: ${{selectedMonth}}`);
            return;
        }}
        
        const currentColors = currentData.labels.map(user => userColors[user] || '#ccc');

        const chartData = {{
            labels: currentData.labels,
            datasets: [{{
                data: currentData.data,
                backgroundColor: currentColors,
                borderWidth: 0,
                hoverOffset: 10
            }}]
        }};

        if (monthlyPieChart) {{
            monthlyPieChart.data = chartData;
            monthlyPieChart.update();
        }} else {{
            const ctx = document.getElementById('monthlyPieChart').getContext('2d');
            monthlyPieChart = new Chart(ctx, {{
                type: 'doughnut',
                data: chartData,
                options: getCommonOptions(true)
            }});
        }}
    }}
    
    // 初始化运行一次
    updateMonthlyPie();

    // --- 应用月份范围 ---
    window.applyMonthRange = function(chartType) {{
        const chartId = chartType === 'monthly' ? 'monthlyChart' : 'dailyChart';
        const startMonth = document.getElementById(`${{chartType}}StartMonth`).value;
        const endMonth = document.getElementById(`${{chartType}}EndMonth`).value;
        
        const chart = charts[chartId];
        const filteredData = filterDataByMonthRange(chartType, startMonth, endMonth);
        
        chart.data = filteredData;
        chart.update();
        
        // 重置缩放
        resetZoom(chartId);
    }};

    // --- 重置缩放 ---
    window.resetZoom = function(chartId) {{
        const chart = charts[chartId];
        if (chart && chart.resetZoom) {{
            chart.resetZoom();
        }}
    }};

    // --- 交互功能函数 ---

    // A. 切换图表类型 (Line / Bar)
    window.changeType = function(chartId, type) {{
        const chart = charts[chartId];
        chart.config.type = type;
        
        // 样式切换逻辑
        document.querySelectorAll(`#btn-${{chartId}}-line, #btn-${{chartId}}-bar`).forEach(b => b.classList.remove('active'));
        document.getElementById(`btn-${{chartId}}-${{type}}`).classList.add('active');

        // Line 模式下去掉填充，Bar 模式下启用
        chart.data.datasets.forEach(ds => {{
            ds.fill = (type === 'bar' && chart.options.scales.x.stacked); 
        }});
        
        chart.update();
    }};

    // B. 切换堆叠模式
    window.toggleStack = function(chartId) {{
        const chart = charts[chartId];
        const btn = document.getElementById(`btn-${{chartId}}-stack`);
        btn.classList.toggle('active');
        const isStacked = btn.classList.contains('active');
        
        chart.options.scales.x.stacked = isStacked;
        chart.options.scales.y.stacked = isStacked;
        chart.update();
    }};

    // C. 全选 / 全不选
    window.toggleAll = function(chartId, visible) {{
        const chart = charts[chartId];
        
        chart.data.datasets.forEach((ds, index) => {{
            chart.setDatasetVisibility(index, visible);
        }});
        
        chart.update();
    }};

</script>
</body>
</html>
"""
        return html_content

    def run(self):
        """Run the dashboard generation process"""
        print("📊 Processing data...")
        data = self.process_data()
        if data:
            html = self.generate_html(data)
            this_dir = os.path.dirname(os.path.abspath(__file__))
            output_dir = os.path.join(this_dir, "..", "dashboard")
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            with open(
                os.path.join(output_dir, "index.html"), "w", encoding="utf-8"
            ) as f:
                f.write(html)
            print(f"✅ Dashboard generated: {output_dir}/index.html")


if __name__ == "__main__":
    this_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file = os.path.join(this_dir, "..", "ssh_login_minutes.csv")

    DashboardGenerator(csv_file).run()
