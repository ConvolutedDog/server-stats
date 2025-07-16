#!/usr/bin/env python3
"""
SSH Session Duration Calculator
- Parses /var/log/secure* files with sudo privileges
- Calculates daily SSH login duration per user
- Supports debug mode for testing specific dates
"""

import os
import re
import sys
import csv
from datetime import datetime, timedelta, time
from collections import defaultdict
from tempfile import NamedTemporaryFile
import argparse


def get_secure_logs():
    """Get list of secure log files (including rotated ones)"""
    sorted_logs = sorted(
        f
        for f in os.listdir("/var/log")
        if f.startswith("secure") and not f.endswith(".tmp")
    )
    for log in sorted_logs:
        print(f"Found log: {log}")
    return sorted_logs


def parse_timestamp(timestamp_str, year_override=None):
    """
    Parse log timestamp with optional year override

    Args:
        timestamp_str: Raw timestamp from log (e.g. "May  7 15:56:16")
        year_override: Force specific year (for debugging), None for current year

    Returns:
        datetime object

    Raises:
        ValueError: If timestamp format is invalid
    """
    try:
        # Determine year to use
        year = year_override if year_override else datetime.now().year
        # Combine with original timestamp
        full_str = f"{year} {timestamp_str.strip()}"
        # Parse standardized format
        return datetime.strptime(full_str, "%Y %b %d %H:%M:%S")
    except Exception as e:
        raise ValueError(f"Failed to parse '{timestamp_str}': {str(e)}")


def parse_secure_logs():
    """
    Parse all SSH session events from secure logs

    Returns:
        dict { (username, pid): [(timestamp, action)] }
    """
    sessions = defaultdict(list)
    year_override = None

    for log_file in get_secure_logs():
        try:
            with os.popen(f"sudo cat /var/log/{log_file}") as f:
                for line in f:
                    match = re.search(
                        r"^(\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}).*?"  # Timestamp
                        r"sshd\[(\d+)\]:.*"  # Pid
                        r"pam_unix\(sshd:session\): session (opened|closed)"  # Event type
                        r" for user (\w+)",  # Username
                        line,
                    )
                    if match:
                        timestamp_str, pid, action, username = match.groups()
                        try:
                            timestamp = parse_timestamp(timestamp_str, year_override)
                            sessions[(username, pid)].append((timestamp, action))
                        except ValueError as e:
                            sys.stderr.write(f"[WARN] {log_file}: {str(e)}\n")
        except Exception as e:
            sys.stderr.write(f"[ERROR] Failed to read {log_file}: {str(e)}\n")

    return sessions


def calculate_daily_usage(sessions, target_date):
    """
    Calculate total SSH presence time per user for target date

    Args:
        sessions: Output from parse_secure_logs(), format: {(user, pid): [(timestamp, action)]}
        target_date: datetime.date object

    Returns:
        dict: {username: timedelta}
    """
    user_sessions = defaultdict(list)

    for (user, pid), events in sessions.items():
        events.sort(key=lambda x: x[0])

        open_time = None
        for ts, action in events:
            if ts.date() != target_date:
                continue

            if action == "opened":
                open_time = ts
            elif action == "closed" and open_time:
                user_sessions[user].append((open_time, ts))
                open_time = None

        # Handle unclosed sessions.
        if open_time:
            # Assuming the session lasts until 23:59:59 or the current
            # time (if the day has not ended).
            end_time = (
                datetime.combine(target_date, time(23, 59, 59))
                if target_date < datetime.now().date()
                else datetime.now()
            )

            user_sessions[user].append((open_time, end_time))

    # Merge.
    result = {}
    for user, intervals in user_sessions.items():
        if not intervals:
            continue

        # Merge overlapping time periods.
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        merged = [sorted_intervals[0]]

        for current_start, current_end in sorted_intervals[1:]:
            last_start, last_end = merged[-1]

            if current_start <= last_end:
                # Time periods overlap, merge.
                merged[-1] = (last_start, max(last_end, current_end))
            else:
                merged.append((current_start, current_end))

        # Calculate the total duration.
        total = sum((end - start).total_seconds() for start, end in merged)
        result[user] = timedelta(seconds=total)

    return result


def get_all_users():
    """Get all system users with UID >= 1000"""
    users = set()
    with os.popen("getent passwd {1000..60000} | cut -d: -f1") as f:
        users.update(line.strip() for line in f if line.strip())
    return users


def generate_report(daily_usage, target_date):
    """Print formatted usage report"""
    print(f"\nSSH Login Duration Report for {target_date.strftime('%Y-%m-%d')}")
    print("=" * 50)
    print("{:<20} {:<10}".format("Username", "Minutes"))
    print("-" * 30)

    all_users = get_all_users()
    for user in sorted(all_users):
        minutes = daily_usage.get(user, timedelta()).total_seconds() / 60
        print("{:<20} {:<10.2f}".format(user, minutes))


def get_existing_usernames(csv_file):
    """Get list of existing usernames from CSV file header"""
    if not os.path.exists(csv_file):
        return []

    with open(csv_file, "r") as f:
        reader = csv.reader(f)
        headers = next(reader, [])
        return headers[1:]  # Exclude first column ('date')


def write_to_csv(daily_usage, target_date):
    """Write login data to CSV file with dynamic header management"""
    this_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file = os.path.join(this_dir, "..", "ssh_login_minutes.csv")

    # Get existing and current usernames
    existing_usernames = get_existing_usernames(csv_file)
    current_usernames = list(daily_usage.keys())

    # Merge username lists
    all_usernames = existing_usernames + [
        user for user in current_usernames if user not in existing_usernames
    ]

    # Prepare row data
    row_data = {"date": target_date.strftime("%Y-%m-%d")}
    for username in all_usernames:
        if username in daily_usage:
            minutes = daily_usage[username]
            row_data[username] = round(
                (
                    minutes.total_seconds() / 60
                    if isinstance(minutes, timedelta)
                    else float(minutes)
                ),
                2,
            )
        else:
            row_data[username] = 0.00

    fieldnames = ["date"] + all_usernames

    # Use temp file in same directory to avoid cross-device issues
    temp_file = None
    try:
        # Create temp file in same directory as target
        temp_path = os.path.join(
            os.path.dirname(csv_file), f"temp_{os.path.basename(csv_file)}"
        )
        temp_file = open(temp_path, "w", newline="")

        writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
        writer.writeheader()

        should_append_row_data = True

        # Copy existing data if file exists
        if os.path.exists(csv_file):
            with open(csv_file, "r") as infile:
                reader = csv.DictReader(infile)
                for row in reader:
                    new_row = {"date": row["date"]}
                    for username in all_usernames:
                        new_row[username] = row.get(username, 0.00)
                    writer.writerow(new_row)

                    # If the date we want to update has been in the csv, either owing to our
                    # pull request or push, we should skip the appending of row_data.
                    if new_row["date"] == row_data["date"]:
                        should_append_row_data = False

        # Write new data
        if should_append_row_data:
            writer.writerow(row_data)
        temp_file.close()

        # Atomic rename within same filesystem
        os.replace(temp_path, csv_file)

    except Exception as e:
        # Clean up temp file if error occurs
        if temp_file and not temp_file.closed:
            temp_file.close()
        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)
        raise e


def main():
    parser = argparse.ArgumentParser(
        description="Calculate daily SSH login duration per user",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--date",
        help="Target date (YYYY-MM-DD), defaults to yesterday",
        default=(datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d"),
    )

    args = parser.parse_args()

    try:
        # Parse logs (with optional debug timestamp override)
        sessions = parse_secure_logs()

        # Calculate usage for target date
        target_date = datetime.strptime(args.date, "%Y-%m-%d").date()
        daily_usage = calculate_daily_usage(sessions, target_date)

        # Generate report
        generate_report(daily_usage, target_date)

        # Write to CSV
        write_to_csv(daily_usage, target_date)
    except Exception as e:
        sys.stderr.write(f"[ERROR] {str(e)}\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
