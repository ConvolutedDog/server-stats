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
|  month  | pengbenkang | yangjianchao | pengyinlun | juxin | hello | shenjunzhong | fengjing | wangjianan | chendong | hejun | yangrenyu | xuezeyu | kangyuhan | lzd | yangjingkui |
|:-------:|:-----------:|:------------:|:----------:|:-----:|:-----:|:------------:|:--------:|:----------:|:--------:|:-----:|:---------:|:-------:|:---------:|:---:|:-----------:|
|  Total  |     26d     |     30d      |    18d     |  15d  |  13d  |     15d      |    3d    |     3d     |    8d    |   3d  |    21d    |   15d   |     7d    |  2d |      1d     |
| 2025-05 |      8      |      11      |     9      |   1   |   4   |      4       |    0     |     0      |    3     |   1   |     8     |    5    |     3     |  1  |      1      |
| 2025-04 |      18     |      19      |     9      |   14  |   9   |      11      |    3     |     3      |    5     |   2   |     13    |    10   |     4     |  1  |      0      |

## Daily login time in minutes for the past 30 days
|    date    | pengbenkang | yangjianchao | pengyinlun | juxin  | hello  | shenjunzhong | fengjing | wangjianan | chendong | hejun  | yangrenyu | xuezeyu | kangyuhan | lzd  | yangjingkui |
|:----------:|:-----------:|:------------:|:----------:|:------:|:------:|:------------:|:--------:|:----------:|:--------:|:------:|:---------:|:-------:|:---------:|:----:|:-----------:|
|   Total    |    120.6h   |    346.4h    |   101.3h   | 101.1h | 34.6h  |    18.8h     |   0.0h   |    0.0h    |   2.2h   |  5.2h  |   108.2h  |  189.9h |   16.8h   | 0.3h |     0.0h    |
| 2025-05-16 |    397.13   |    796.28    |   745.52   |  0.0   | 247.23 |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |   181.12  |   0.0   |    0.0    | 0.0  |     0.0     |
| 2025-05-15 |    663.3    |    926.62    |   680.45   |  0.0   |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |   312.47  |   0.0   |    0.0    | 0.0  |     0.0     |
| 2025-05-14 |    611.4    |   1049.63    |   684.9    |  0.0   |  0.0   |    16.25     |   0.0    |    0.0     |  15.17   |  0.0   |   249.57  |  1306.4 |    0.0    | 0.0  |     0.05    |
| 2025-05-13 |    428.08   |    851.9     |   685.35   |  0.0   | 212.02 |     0.0      |   0.0    |    0.0     |   0.0    | 309.67 |   484.43  |  295.02 |   314.58  | 6.03 |     0.0     |
| 2025-05-12 |    533.78   |   1394.52    |   559.22   |  0.0   | 412.45 |     0.75     |   0.0    |    0.0     |   0.0    |  0.0   |   554.85  |  303.02 |   230.2   | 0.0  |     0.0     |
| 2025-05-11 |    464.57   |    435.37    |   218.13   |  0.0   |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    | 0.0  |     0.0     |
| 2025-05-10 |    269.07   |   1149.55    |   507.92   |  0.0   |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    | 0.0  |     0.0     |
| 2025-05-09 |     0.0     |    1077.8    |   163.6    |  0.0   | 146.88 |     0.0      |   0.0    |    0.0     |   2.2    |  0.0   |   93.03   |   0.0   |   11.52   | 0.0  |     0.0     |
| 2025-05-08 |     0.0     |   1110.37    |    0.0     | 541.13 |  0.0   |    10.38     |   0.0    |    0.0     |   0.0    |  0.0   |   158.28  |  525.03 |    0.0    | 0.0  |     0.0     |
| 2025-05-07 |     5.88    |    483.15    |   282.15   |  0.0   |  0.0   |     0.68     |   0.0    |    0.0     |   5.48   |  0.0   |   255.07  |  417.92 |    0.0    | 0.0  |     0.0     |
| 2025-05-06 |     0.0     |     0.0      |    0.0     |  0.0   |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    | 0.0  |     0.0     |
| 2025-05-05 |     0.0     |     0.0      |    0.0     |  0.0   |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    | 0.0  |     0.0     |
| 2025-05-04 |     0.0     |     0.0      |    0.0     |  0.0   |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    | 0.0  |     0.0     |
| 2025-05-03 |     0.0     |     0.0      |    0.0     |  0.0   |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    | 0.0  |     0.0     |
| 2025-05-02 |     0.0     |     0.0      |    0.0     |  0.0   |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    | 0.0  |     0.0     |
| 2025-05-01 |     0.0     |   1415.33    |    0.0     |  0.0   |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    | 0.0  |     0.0     |
| 2025-04-30 |    253.17   |    666.58    |   256.25   |  0.0   |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |   159.57  |   0.0   |    0.0    | 0.0  |     0.0     |
| 2025-04-29 |    45.77    |    890.88    |   357.93   | 47.65  |  0.0   |    73.08     |   0.0    |    0.0     |   0.0    |  0.0   |   466.27  | 1208.12 |    0.0    | 0.0  |     0.0     |
| 2025-04-28 |     7.13    |   1166.22    |   350.63   |  0.0   |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |   599.4   |   0.0   |    0.0    | 0.0  |     0.0     |
| 2025-04-27 |    531.18   |    589.4     |   475.92   |  0.0   | 130.65 |    118.92    |   0.0    |    0.0     |   0.0    |  0.0   |   502.98  | 1346.75 |    0.0    | 9.03 |     0.0     |
| 2025-04-26 |    353.8    |   1139.15    |    0.0     | 759.98 |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   2.6   |    0.0    | 0.0  |     0.0     |
| 2025-04-25 |    356.67   |   1339.65    |    0.0     | 916.08 | 186.8  |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |   318.28  |   0.0   |    0.0    | 0.0  |     0.0     |
| 2025-04-24 |    138.77   |    781.47    |    0.0     | 695.5  | 200.02 |     0.0      |   0.0    |    0.0     |  101.88  |  0.0   |   453.77  | 1426.93 |    0.0    | 0.0  |     0.0     |
| 2025-04-23 |    397.08   |    1353.9    |    0.0     | 745.08 |  0.0   |     0.37     |   0.0    |    0.0     |   0.0    |  0.0   |   302.38  | 1415.23 |    0.0    | 0.0  |     0.0     |
| 2025-04-22 |    151.67   |    451.2     |   110.25   | 357.58 | 326.48 |    164.32    |   0.0    |    0.0     |   0.0    |  0.0   |   346.72  |   0.0   |    0.0    | 0.0  |     0.0     |
| 2025-04-21 |    392.98   |    323.95    |    0.0     | 698.85 | 212.53 |    267.8     |   0.0    |    0.0     |   0.0    |  0.0   |   379.83  |  932.13 |    0.0    | 0.0  |     0.0     |
| 2025-04-20 |    564.45   |    56.33     |    0.0     |  0.0   |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |  692.93 |   20.67   | 0.0  |     0.0     |
| 2025-04-19 |    423.37   |   1172.27    |    0.0     | 474.82 |  0.0   |    190.1     |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    | 0.0  |     0.0     |
| 2025-04-18 |    247.95   |    44.17     |    0.0     | 557.52 |  0.0   |    156.47    |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    | 1084.15 |   295.35  | 0.0  |     0.0     |
| 2025-04-17 |     0.0     |    116.53    |    0.0     | 270.65 |  0.0   |    127.02    |   0.0    |    0.0     |   5.32   |  0.0   |   671.93  |  438.45 |   133.67  | 0.0  |     0.0     |

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
