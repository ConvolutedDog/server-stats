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
  Ref: scripts/transfer-csv-to-readme.py
-->
## Monthly login time in days
|  month  | pengbenkang | yangjianchao | pengyinlun | juxin | hello | shenjunzhong | fengjing | wangjianan | chendong | hejun | yangrenyu | xuezeyu | kangyuhan | lzd |
|:-------:|:-----------:|:------------:|:----------:|:-----:|:-----:|:------------:|:--------:|:----------:|:--------:|:-----:|:---------:|:-------:|:---------:|:---:|
|  Total  |     19d     |     21d      |    10d     |  14d  |   9d  |     12d      |    3d    |     3d     |    6d    |   2d  |    14d    |   11d   |     4d    |  1d |
| 2025-05 |      1      |      2       |     1      |   0   |   0   |      1       |    0     |     0      |    1     |   0   |     1     |    1    |     0     |  0  |
| 2025-04 |      18     |      19      |     9      |   14  |   9   |      11      |    3     |     3      |    5     |   2   |     13    |    10   |     4     |  1  |

## Daily login time in minutes for the past 30 days
|    date    | pengbenkang | yangjianchao | pengyinlun | juxin  | hello  | shenjunzhong | fengjing | wangjianan | chendong | hejun  | yangrenyu | xuezeyu | kangyuhan | lzd  |
|:----------:|:-----------:|:------------:|:----------:|:------:|:------:|:------------:|:--------:|:----------:|:--------:|:------:|:---------:|:-------:|:---------:|:----:|
|   Total    |    66.9h    |    227.4h    |   46.7h    | 115.2h | 25.0h  |    20.2h     |  14.0h   |   26.9h    |   3.3h   |  3.8h  |   89.7h   |  150.0h |    9.0h   | 0.2h |
| 2025-05-07 |     5.88    |    483.15    |   282.15   |  0.0   |  0.0   |     0.68     |   0.0    |    0.0     |   5.48   |  0.0   |   255.07  |  417.92 |    0.0    | 0.0  |
| 2025-05-06 |     0.0     |     0.0      |    0.0     |  0.0   |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    | 0.0  |
| 2025-05-05 |     0.0     |     0.0      |    0.0     |  0.0   |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    | 0.0  |
| 2025-05-04 |     0.0     |     0.0      |    0.0     |  0.0   |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    | 0.0  |
| 2025-05-03 |     0.0     |     0.0      |    0.0     |  0.0   |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    | 0.0  |
| 2025-05-02 |     0.0     |     0.0      |    0.0     |  0.0   |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    | 0.0  |
| 2025-05-01 |     0.0     |   1415.33    |    0.0     |  0.0   |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    | 0.0  |
| 2025-04-30 |    253.17   |    666.58    |   256.25   |  0.0   |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |   159.57  |   0.0   |    0.0    | 0.0  |
| 2025-04-29 |    45.77    |    890.88    |   357.93   | 47.65  |  0.0   |    73.08     |   0.0    |    0.0     |   0.0    |  0.0   |   466.27  | 1208.12 |    0.0    | 0.0  |
| 2025-04-28 |     7.13    |   1166.22    |   350.63   |  0.0   |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |   599.4   |   0.0   |    0.0    | 0.0  |
| 2025-04-27 |    531.18   |    589.4     |   475.92   |  0.0   | 130.65 |    118.92    |   0.0    |    0.0     |   0.0    |  0.0   |   502.98  | 1346.75 |    0.0    | 9.03 |
| 2025-04-26 |    353.8    |   1139.15    |    0.0     | 759.98 |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   2.6   |    0.0    | 0.0  |
| 2025-04-25 |    356.67   |   1339.65    |    0.0     | 916.08 | 186.8  |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |   318.28  |   0.0   |    0.0    | 0.0  |
| 2025-04-24 |    138.77   |    781.47    |    0.0     | 695.5  | 200.02 |     0.0      |   0.0    |    0.0     |  101.88  |  0.0   |   453.77  | 1426.93 |    0.0    | 0.0  |
| 2025-04-23 |    397.08   |    1353.9    |    0.0     | 745.08 |  0.0   |     0.37     |   0.0    |    0.0     |   0.0    |  0.0   |   302.38  | 1415.23 |    0.0    | 0.0  |
| 2025-04-22 |    151.67   |    451.2     |   110.25   | 357.58 | 326.48 |    164.32    |   0.0    |    0.0     |   0.0    |  0.0   |   346.72  |   0.0   |    0.0    | 0.0  |
| 2025-04-21 |    392.98   |    323.95    |    0.0     | 698.85 | 212.53 |    267.8     |   0.0    |    0.0     |   0.0    |  0.0   |   379.83  |  932.13 |    0.0    | 0.0  |
| 2025-04-20 |    564.45   |    56.33     |    0.0     |  0.0   |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |  692.93 |   20.67   | 0.0  |
| 2025-04-19 |    423.37   |   1172.27    |    0.0     | 474.82 |  0.0   |    190.1     |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    | 0.0  |
| 2025-04-18 |    247.95   |    44.17     |    0.0     | 557.52 |  0.0   |    156.47    |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    | 1084.15 |   295.35  | 0.0  |
| 2025-04-17 |     0.0     |    116.53    |    0.0     | 270.65 |  0.0   |    127.02    |   0.0    |    0.0     |   5.32   |  0.0   |   671.93  |  438.45 |   133.67  | 0.0  |
| 2025-04-16 |     37.3    |    567.73    |   466.73   | 907.92 | 59.87  |     3.37     |   0.0    |   463.62   |  24.12   |  0.23  |   239.45  |   0.0   |   91.57   | 0.0  |
| 2025-04-15 |    37.15    |    471.1     |   299.92   | 69.35  | 143.12 |     0.0      |  31.93   |   459.73   |   7.97   |  0.0   |   462.53  |   32.9  |    0.0    | 0.0  |
| 2025-04-14 |    72.63    |    612.77    |   204.07   | 410.27 | 243.5  |    112.63    |  807.52  |   692.23   |  50.42   | 230.33 |   223.6   |   0.0   |    0.0    | 0.0  |
| 2025-04-13 |     0.0     |     0.0      |    0.0     |  0.0   |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    | 0.0  |
| 2025-04-12 |     0.0     |     0.0      |    0.0     |  0.0   |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    | 0.0  |
| 2025-04-11 |     0.0     |     0.0      |    0.0     |  0.0   |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    | 0.0  |
| 2025-04-10 |     0.0     |     0.0      |    0.0     |  0.0   |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    | 0.0  |
| 2025-04-09 |     0.0     |     0.0      |    0.0     |  0.0   |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    | 0.0  |
| 2025-04-08 |     0.0     |     0.0      |    0.0     |  0.0   |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    | 0.0  |

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
