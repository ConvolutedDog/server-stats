#!/usr/bin/env python3
"""
CSV to README Reansfer
- Read ../ssh_login_minutes.csv
- Transfer to Markdown
- Write to README.md
"""

import csv
import re
from pathlib import Path
from datetime import datetime

def csv_to_markdown(csv_path, num_rows=100):
    """Convert CSV to Markdown table with newest dates first and proper column widths"""
    with open(csv_path, 'r') as f:
        reader = csv.reader(f)
        headers = next(reader)
        data = list(reader)
    
    # Sort by date (newest first)
    try:
        def parse_date(date_str):
            for fmt in ('%Y-%m-%d', '%m/%d/%Y', '%d/%m/%Y'):
                try:
                    return datetime.strptime(date_str, fmt)
                except ValueError:
                    continue
            return datetime.min
        
        data.sort(key=lambda x: parse_date(x[0]), reverse=True)
    except Exception as e:
        print(f"Warning: Could not sort by date - {str(e)}")
        data = data[-num_rows:]
    
    # Get only the most recent rows
    recent_data = data[:num_rows]
    
    # Calculate max width for each column
    col_widths = [len(header) for header in headers]
    for row in recent_data:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(cell)))
    
    # Create markdown table with proper spacing
    table = ""

    # Header row
    header_row = "|"
    for i, header in enumerate(headers):
        header_row += f" {header.center(col_widths[i])} |"
    table += header_row + "\n"
    
    # Separator row
    separator_row = "|"
    for width in col_widths:
        separator_row += f":{'-'*(width)}:" if width > 2 else ":-:"
        separator_row += "|"
    table += separator_row + "\n"
    
    # Data rows
    for row in recent_data:
        data_row = "|"
        for i, cell in enumerate(row):
            data_row += f" {str(cell).center(col_widths[i])} |"
        table += data_row + "\n"

    return table.strip()

def update_readme(readme_path, new_content):
    """Update README.md between specified headers"""
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    print(new_content)
    # Replace content between headers
    pattern = r'(## Daily login time in minutes\n).*?(\n##\s)'
    replacement = r'\1' + new_content + '\n' + r'\2'
    updated_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    print(updated_content)
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)

def main():
    base_dir = Path(__file__).parent.parent
    csv_path = base_dir / 'ssh_login_minutes.csv'
    readme_path = base_dir / 'README.md'
    
    if not csv_path.exists():
        print(f"Error: {csv_path} not found")
        return
    
    try:
        markdown_table = csv_to_markdown(csv_path)
        update_readme(readme_path, markdown_table)
        print("Successfully updated README with newest login data")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
