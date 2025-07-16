#!/usr/bin/env python3
"""
CSV to README Reansfer
- Read ../ssh_login_minutes.csv
- Transfer to Markdown
- Write to README.md
"""

import os
import csv
import re
from collections import defaultdict
from datetime import datetime


def csv_to_markdown_monthly(csv_path):
    """Convert CSV to Markdown table with newest months first and proper column widths"""
    with open(csv_path, "r") as f:
        reader = csv.reader(f)
        headers = next(reader)
        users = headers[1:]  # Skip the first column (date)

        monthly_usage = defaultdict(lambda: defaultdict(int))
        user_totals = defaultdict(int)

        for row in reader:

            date_str = row[0]
            date = datetime.strptime(date_str, "%Y-%m-%d")
            month_key = f"{date.year}-{date.month:02d}"

            for i, value_str in enumerate(row[1:], start=1):
                value = float(value_str)
                if value > 0:
                    username = users[i - 1]
                    monthly_usage[month_key][username] += 1
                    user_totals[username] += 1

        # for month, user_stats in monthly_usage.items():
        #     print(f"Month: {month}")
        #     for user, days in user_stats.items():
        #         print(f"  {user}: {days} days")

        # Sort
        all_months = sorted(monthly_usage.keys(), reverse=True)
        table_headers = ["month"] + users

        # Generate data rows
        table_rows = []

        for month in all_months:
            row = [month]
            for user in users:
                row.append(str(monthly_usage[month].get(user, 0)))
            table_rows.append(row)

        # Generate total row
        total_row = ["Total"] + [
            (str(user_totals.get(user, 0)) + "d") for user in users
        ]

        # Calculate max width for each column
        col_widths = [len(header) for header in table_headers]
        for row in table_rows + [total_row]:
            for i, cell in enumerate(row):
                col_widths[i] = max(col_widths[i], len(str(cell)))

        # Create markdown table with proper spacing
        table = ""

        # Header row
        header_row = "|"
        for i, header in enumerate(table_headers):
            header_row += f" {header.center(col_widths[i])} |"
        tableheader = header_row + "\n"

        # Separator row
        separator_row = "|"
        for width in col_widths:
            separator_row += f":{'-'*(width)}:" if width > 2 else ":-:"
            separator_row += "|"
        tableseparator = separator_row + "\n"

        # Data rows
        for row in table_rows:
            data_row = "|"
            for i, cell in enumerate(row):
                data_row += f" {str(cell).center(col_widths[i])} |"
            table += data_row + "\n"

        # Add total row
        total_data_row = "|"
        for i, cell in enumerate(total_row):
            total_data_row += f" {str(cell).center(col_widths[i])} |"

        tablewithtotal = tableheader + tableseparator + total_data_row + "\n"
        tablewithtotal += table

        return tablewithtotal.strip()


def csv_to_markdown_daily(csv_path, num_rows=30):
    """Convert CSV to Markdown table with newest dates first and proper column widths"""
    with open(csv_path, "r") as f:
        reader = csv.reader(f)
        headers = next(reader)
        data = list(reader)

    # Sort by date (newest first)
    try:

        def parse_date(date_str):
            for fmt in ("%Y-%m-%d", "%m/%d/%Y", "%d/%m/%Y"):
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

    # Calculate totals for each user (skip date column)
    user_totals = []
    for col in range(1, len(headers)):
        try:
            total_minutes = sum(float(row[col]) for row in recent_data)
            total_hours = round(total_minutes / 60, 1)
            user_totals.append(f"{total_hours}h")
        except:
            user_totals.append("N/A")

    # Create the "Total" row
    total_row = ["Total"] + user_totals

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
    tableheader = header_row + "\n"

    # Separator row
    separator_row = "|"
    for width in col_widths:
        separator_row += f":{'-'*(width)}:" if width > 2 else ":-:"
        separator_row += "|"
    tableseparator = separator_row + "\n"

    # Data rows
    for row in recent_data:
        data_row = "|"
        for i, cell in enumerate(row):
            data_row += f" {str(cell).center(col_widths[i])} |"
        table += data_row + "\n"

    # Add total rows per user
    total_data_row = "|"
    for i, cell in enumerate(total_row):
        total_data_row += f" {str(cell).center(col_widths[i])} |"

    tablewithtotal = tableheader + tableseparator + total_data_row + "\n"
    tablewithtotal += table

    return tablewithtotal.strip()


def update_readme_daily(readme_path, new_content):
    """Update README.md between specified headers"""
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()
    print(new_content)
    # Replace content between headers
    pattern = r"(## Daily login time in minutes for the past 30 days\n).*?(\n##\s)"
    replacement = r"\1" + new_content + "\n" + r"\2"
    updated_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(updated_content)


def update_readme_monthly(readme_path, new_content):
    """Update README.md between specified headers"""
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()
    print(new_content)
    # Replace content between headers
    pattern = r"(## Monthly login time in days\n).*?(\n##\s)"
    replacement = r"\1" + new_content + "\n" + r"\2"
    updated_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(updated_content)


def main():
    this_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.join(this_dir, "..")

    csv_path = os.path.join(base_dir, "ssh_login_minutes.csv")
    readme_path = os.path.join(base_dir, "README.md")

    if not os.path.exists(csv_path):
        print(f"Error: {csv_path} not found")
        return
    if not os.path.exists(readme_path):
        print(f"Error: {readme_path} not found")
        return

    try:
        markdown_table_daily = csv_to_markdown_daily(csv_path)
        update_readme_daily(readme_path, markdown_table_daily)

        markdown_table_monthly = csv_to_markdown_monthly(csv_path)
        update_readme_monthly(readme_path, markdown_table_monthly)
        print("Successfully updated README with newest login data")
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
