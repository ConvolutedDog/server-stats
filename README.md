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
|  month  | pengbenkang | yangjianchao | pengyinlun | juxin | hello | shenjunzhong | fengjing | wangjianan | chendong | hejun | yangrenyu | xuezeyu | kangyuhan | lzd | yangjingkui | tangminjin |
|:-------:|:-----------:|:------------:|:----------:|:-----:|:-----:|:------------:|:--------:|:----------:|:--------:|:-----:|:---------:|:-------:|:---------:|:---:|:-----------:|:----------:|
|  Total  |     37d     |     41d      |    23d     |  20d  |  16d  |     20d      |    3d    |     5d     |   14d    |   3d  |    29d    |   20d   |     8d    |  3d |      3d     |     1d     |
| 2025-05 |      19     |      22      |     14     |   6   |   7   |      9       |    0     |     2      |    9     |   1   |     16    |    10   |     4     |  2  |      3      |     1      |
| 2025-04 |      18     |      19      |     9      |   14  |   9   |      11      |    3     |     3      |    5     |   2   |     13    |    10   |     4     |  1  |      0      |     0      |

## Daily login time in minutes for the past 30 days
|    date    | pengbenkang | yangjianchao | pengyinlun |  juxin  | hello  | shenjunzhong | fengjing | wangjianan | chendong | hejun  | yangrenyu | xuezeyu | kangyuhan | lzd  | yangjingkui | tangminjin |
|:----------:|:-----------:|:------------:|:----------:|:-------:|:------:|:------------:|:--------:|:----------:|:--------:|:------:|:---------:|:-------:|:---------:|:----:|:-----------:|:----------:|
|   Total    |    144.1h   |    373.8h    |   159.0h   |  80.2h  | 20.6h  |    23.9h     |   0.0h   |    6.9h    |  17.9h   |  5.2h  |   143.5h  |  111.5h |   10.0h   | 0.5h |     3.2h    |    0.1h    |
| 2025-05-27 |    578.88   |    547.13    |    0.0     |   0.0   |  0.0   |    225.83    |   0.0    |    0.0     |  194.22  |  0.0   |  1389.87  | 1237.58 |    0.0    | 25.0 |     0.0     |    6.0     |
| 2025-05-26 |    276.82   |    400.88    |    0.0     |   0.0   |  0.0   |    419.62    |   0.0    |    0.0     |  491.17  |  0.0   |   607.12  |  78.42  |    0.0    | 0.0  |     0.0     |    0.0     |
| 2025-05-25 |    551.77   |   1145.48    |   222.18   |   0.0   |  0.0   |    239.12    |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    | 0.0  |     0.0     |    0.0     |
| 2025-05-24 |    630.75   |    891.53    |  1316.82   |  386.73 |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |   512.78  |   0.0   |    0.0    | 0.0  |     0.0     |    0.0     |
| 2025-05-23 |    198.03   |    726.1     |  1317.83   | 1384.22 |  0.0   |    246.85    |   0.0    |    0.0     |   0.0    |  0.0   |   677.12  |   0.0   |    0.0    | 0.0  |     0.0     |    0.0     |
| 2025-05-22 |    530.82   |   1224.23    |    0.0     |  679.3  | 90.33  |    200.03    |   0.0    |    0.0     |  295.0   |  0.0   |   176.47  |   0.0   |    0.0    | 0.0  |    174.15   |    0.0     |
| 2025-05-21 |    458.15   |    699.28    |    0.0     |  892.17 |  0.0   |     0.0      |   0.0    |   150.15   |   7.75   |  0.0   |   227.58  |  480.35 |   45.55   | 0.0  |    19.08    |    0.0     |
| 2025-05-20 |    518.77   |    872.23    |    0.0     |  880.95 | 96.25  |     0.0      |   0.0    |   265.1    |   8.68   |  0.0   |   899.13  |  405.45 |    0.0    | 0.0  |     0.0     |    0.0     |
| 2025-05-19 |    525.58   |   1323.85    |    0.0     |   0.0   | 30.08  |     0.0      |   0.0    |    0.0     |  52.62   |  0.0   |   605.1   |  433.93 |    0.0    | 0.0  |     0.0     |    0.0     |
| 2025-05-18 |    278.13   |    216.8     |   430.72   |   0.0   |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    | 0.0  |     0.0     |    0.0     |
| 2025-05-17 |    420.43   |    966.4     |   757.97   |   0.0   |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    | 0.0  |     0.0     |    0.0     |
| 2025-05-16 |    397.13   |    796.28    |   745.52   |   0.0   | 247.23 |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |   181.12  |   0.0   |    0.0    | 0.0  |     0.0     |    0.0     |
| 2025-05-15 |    663.3    |    926.62    |   680.45   |   0.0   |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |   312.47  |   0.0   |    0.0    | 0.0  |     0.0     |    0.0     |
| 2025-05-14 |    611.4    |   1049.63    |   684.9    |   0.0   |  0.0   |    16.25     |   0.0    |    0.0     |  15.17   |  0.0   |   249.57  |  1306.4 |    0.0    | 0.0  |     0.05    |    0.0     |
| 2025-05-13 |    428.08   |    851.9     |   685.35   |   0.0   | 212.02 |     0.0      |   0.0    |    0.0     |   0.0    | 309.67 |   484.43  |  295.02 |   314.58  | 6.03 |     0.0     |    0.0     |
| 2025-05-12 |    533.78   |   1394.52    |   559.22   |   0.0   | 412.45 |     0.75     |   0.0    |    0.0     |   0.0    |  0.0   |   554.85  |  303.02 |   230.2   | 0.0  |     0.0     |    0.0     |
| 2025-05-11 |    464.57   |    435.37    |   218.13   |   0.0   |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    | 0.0  |     0.0     |    0.0     |
| 2025-05-10 |    269.07   |   1149.55    |   507.92   |   0.0   |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    | 0.0  |     0.0     |    0.0     |
| 2025-05-09 |     0.0     |    1077.8    |   163.6    |   0.0   | 146.88 |     0.0      |   0.0    |    0.0     |   2.2    |  0.0   |   93.03   |   0.0   |   11.52   | 0.0  |     0.0     |    0.0     |
| 2025-05-08 |     0.0     |   1110.37    |    0.0     |  541.13 |  0.0   |    10.38     |   0.0    |    0.0     |   0.0    |  0.0   |   158.28  |  525.03 |    0.0    | 0.0  |     0.0     |    0.0     |
| 2025-05-07 |     5.88    |    483.15    |   282.15   |   0.0   |  0.0   |     0.68     |   0.0    |    0.0     |   5.48   |  0.0   |   255.07  |  417.92 |    0.0    | 0.0  |     0.0     |    0.0     |
| 2025-05-06 |     0.0     |     0.0      |    0.0     |   0.0   |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    | 0.0  |     0.0     |    0.0     |
| 2025-05-05 |     0.0     |     0.0      |    0.0     |   0.0   |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    | 0.0  |     0.0     |    0.0     |
| 2025-05-04 |     0.0     |     0.0      |    0.0     |   0.0   |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    | 0.0  |     0.0     |    0.0     |
| 2025-05-03 |     0.0     |     0.0      |    0.0     |   0.0   |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    | 0.0  |     0.0     |    0.0     |
| 2025-05-02 |     0.0     |     0.0      |    0.0     |   0.0   |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    | 0.0  |     0.0     |    0.0     |
| 2025-05-01 |     0.0     |   1415.33    |    0.0     |   0.0   |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    | 0.0  |     0.0     |    0.0     |
| 2025-04-30 |    253.17   |    666.58    |   256.25   |   0.0   |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |   159.57  |   0.0   |    0.0    | 0.0  |     0.0     |    0.0     |
| 2025-04-29 |    45.77    |    890.88    |   357.93   |  47.65  |  0.0   |    73.08     |   0.0    |    0.0     |   0.0    |  0.0   |   466.27  | 1208.12 |    0.0    | 0.0  |     0.0     |    0.0     |
| 2025-04-28 |     7.13    |   1166.22    |   350.63   |   0.0   |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |   599.4   |   0.0   |    0.0    | 0.0  |     0.0     |    0.0     |

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
3. Clear the data in `ssh_login_minutes.csv`, otherwise it will cause your data to contain existing data from this repository:
   ```bash
   echo "" > ssh_login_minutes.csv
   ```
4. The workflow will start automatically at 00:00 (UTC+8) either you can start it using `git push` or manually.
   The workflow that starts automatically will not conflict with data from other startup methods.

## Other methods
- `ac` (accounting) can be used to count the login time of a user (with UTMP/WTMP logs enabled), but it does not distinguish between TTY and SSHD.
