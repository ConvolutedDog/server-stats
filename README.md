# SSH Session Time Report (Daily/Monthly Automation)

This repository automatically collects and processes user login time statistics from Linux servers,
generating daily and monthly reports. The workflow runs daily at 00:00 (UTC+8) to:
- Collect login time data from server logs
- Process statistics through Python scripts on the target server
- Generate CSV reports and update this README file
- Commit changes back to the repository

<!-- 
  NOTE: If you need to modify the section titles of the following tables, 
  you must also update the corresponding Python files to maintain consistency.
-->
## Monthly login time in days
|  month  | xuezeyu | yangjianchao | pengyinlun | yangrenyu | pengbenkang | shenjunzhong | chendong |
|:-------:|:-------:|:------------:|:----------:|:---------:|:-----------:|:------------:|:--------:|
| 2025-05 |    1    |      1       |     1      |     1     |      1      |      1       |    1     |

## Daily login time in minutes
|    date    | xuezeyu | yangjianchao | pengyinlun | yangrenyu | pengbenkang | shenjunzhong | chendong |
|:----------:|:-------:|:------------:|:----------:|:---------:|:-----------:|:------------:|:--------:|
| 2025-05-07 |  417.92 |    483.15    |   282.15   |   255.07  |     5.88    |     0.68     |   5.48   |
| 2025-05-06 |   0.0   |     0.0      |    0.0     |    0.0    |     0.0     |     0.0      |   0.0    |

## Custom Configurations
1. Secrets Configuration
  - `SSH_PRIVATE_KEY`: Private SSH key for authenticating with the target server.
  - `SSH_USERNAME`: Username for SSH authentication on the target server.
  - `SERVER_HOST`: Hostname or IP address of the target server.
  - `SSH_PORT` (Optional): Port number for SSH connection (default: 22).
2. Sudo Requirements
  - The specified SSH user must have the following sudo capabilities (the workflow will copy this repo into the `/tmp/server-stats` directory):
    - Ability to execute the required Python scripts without password prompt (sudo privileges)
      ```bash
      python3 /tmp/server-stats/scripts/count-user-login-minutes-every-day.py
      python3 /tmp/server-stats/scripts/transfer-csv-to-readme.py
      ```
    - Ability to remove the temporary directory after execution:
      ```bash
      rm -rf /tmp/server-stats
      ```

## Other methods
- `ac` (accounting) can be used to count the login time of a user (with UTMP/WTMP logs enabled), but it does not distinguish between TTY and SSHD.
