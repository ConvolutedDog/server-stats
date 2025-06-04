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
|  Total  |     45d     |     49d      |    24d     |  23d  |  19d  |     20d      |    3d    |     6d     |   22d    |   3d  |    34d    |   23d   |    11d    |  3d |      8d     |     1d     |
| 2025-06 |      4      |      4       |     0      |   1   |   1   |      0       |    0     |     0      |    4     |   0   |     2     |    2    |     0     |  0  |      2      |     0      |
| 2025-05 |      23     |      26      |     15     |   8   |   9   |      9       |    0     |     3      |    13    |   1   |     19    |    11   |     7     |  2  |      6      |     1      |
| 2025-04 |      18     |      19      |     9      |   14  |   9   |      11      |    3     |     3      |    5     |   2   |     13    |    10   |     4     |  1  |      0      |     0      |

## Daily login time in minutes for the past 30 days
|    date    | pengbenkang | yangjianchao | pengyinlun |  juxin  | hello  | shenjunzhong | fengjing | wangjianan | chendong | hejun  | yangrenyu | xuezeyu | kangyuhan | lzd  | yangjingkui | tangminjin |
|:----------:|:-----------:|:------------:|:----------:|:-------:|:------:|:------------:|:--------:|:----------:|:--------:|:------:|:---------:|:-------:|:---------:|:----:|:-----------:|:----------:|
|   Total    |    197.4h   |    390.8h    |   145.0h   |  113.4h | 24.6h  |    22.7h     |   0.0h   |    7.0h    |  92.8h   |  5.2h  |   174.3h  |  110.4h |   17.3h   | 0.5h |    14.9h    |    0.1h    |
| 2025-06-04 |    282.1    |   1372.17    |    0.0     |   0.0   |  25.3  |     0.0      |   0.0    |    0.0     |  627.7   |  0.0   |   911.03  |  630.15 |    0.0    | 0.0  |    217.17   |    0.0     |
| 2025-06-03 |    461.53   |   1423.38    |    0.0     |   0.0   |  0.0   |     0.0      |   0.0    |    0.0     |  858.97  |  0.0   |   631.77  |  130.93 |    0.0    | 0.0  |    166.07   |    0.0     |
| 2025-06-02 |    663.52   |    161.28    |    0.0     |   0.0   |  0.0   |     0.0      |   0.0    |    0.0     |  251.12  |  0.0   |    0.0    |   0.0   |    0.0    | 0.0  |     0.0     |    0.0     |
| 2025-06-01 |    632.93   |     0.68     |    0.0     |  169.27 |  0.0   |     0.0      |   0.0    |    0.0     |  141.57  |  0.0   |    0.0    |   0.0   |    0.0    | 0.0  |     0.0     |    0.0     |
| 2025-05-31 |    101.87   |     0.55     |    0.0     | 1066.13 |  0.0   |     0.0      |   0.0    |    0.0     |  105.6   |  0.0   |    0.0    |   0.0   |    0.0    | 0.0  |     0.0     |    0.0     |
| 2025-05-30 |    148.92   |    570.93    |   127.93   |  802.22 |  43.5  |     0.0      |   0.0    |    0.0     | 1069.93  |  0.0   |   530.48  |   0.0   |   165.08  | 0.0  |    139.0    |    0.0     |
| 2025-05-29 |    602.33   |    869.25    |    0.0     |   0.0   |  0.0   |     0.0      |   0.0    |    4.97    |  692.02  |  0.0   |   634.77  |  380.43 |   239.78  | 0.0  |    108.88   |    0.0     |
| 2025-05-28 |    608.73   |    763.42    |    0.0     |   0.0   | 172.6  |     0.0      |   0.0    |    0.0     |  746.85  |  0.0   |   367.2   |   0.0   |   28.97   | 0.0  |    71.47    |    0.0     |
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
