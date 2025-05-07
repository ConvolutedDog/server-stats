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
    """Convert CSV to Markdown table with newest dates first"""
    with open(csv_path, 'r') as f:
        reader = csv.reader(f)
        headers = next(reader)
        data = list(reader)
    
    # Sort by date (newest first)
    try:
        # Try to parse dates in multiple common formats
        def parse_date(date_str):
            for fmt in ('%Y-%m-%d', '%m/%d/%Y', '%d/%m/%Y'):
                try:
                    return datetime.strptime(date_str, fmt)
                except ValueError:
                    continue
            return datetime.min  # If all formats fail
        
        data.sort(key=lambda x: parse_date(x[0]), reverse=True)
    except Exception as e:
        print(f"Warning: Could not sort by date - {str(e)}")
        data = data[-num_rows:]  # Fallback: take last 100 rows
    
    # Get only the most recent rows
    recent_data = data[:num_rows]
    
    # Create markdown table with centered alignment
    table = "| " + " | ".join(headers) + " |\n"
    table += "|" + "|".join([":---:"] * len(headers)) + "|\n"
    for row in recent_data:
        table += "| " + " | ".join(row) + " |\n"
    
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
