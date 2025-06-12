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
|  Total  |     52d     |     56d      |    25d     |  29d  |  22d  |     26d      |    4d    |     6d     |   29d    |   3d  |    38d    |   28d   |    14d    |  6d |     11d     |     1d     |
| 2025-06 |      11     |      11      |     1      |   7   |   4   |      6       |    1     |     0      |    11    |   0   |     6     |    7    |     3     |  3  |      5      |     0      |
| 2025-05 |      23     |      26      |     15     |   8   |   9   |      9       |    0     |     3      |    13    |   1   |     19    |    11   |     7     |  2  |      6      |     1      |
| 2025-04 |      18     |      19      |     9      |   14  |   9   |      11      |    3     |     3      |    5     |   2   |     13    |    10   |     4     |  1  |      0      |     0      |

## Daily login time in minutes for the past 30 days
|    date    | pengbenkang | yangjianchao | pengyinlun |  juxin  | hello  | shenjunzhong | fengjing | wangjianan | chendong | hejun  | yangrenyu | xuezeyu | kangyuhan |  lzd  | yangjingkui | tangminjin |
|:----------:|:-----------:|:------------:|:----------:|:-------:|:------:|:------------:|:--------:|:----------:|:--------:|:------:|:---------:|:-------:|:---------:|:-----:|:-----------:|:----------:|
|   Total    |    227.9h   |    419.5h    |   119.6h   |  170.5h | 19.2h  |    42.0h     |   0.1h   |    7.0h    |  169.5h  |  5.2h  |   187.0h  |  147.2h |   35.4h   |  0.8h |    17.5h    |    0.1h    |
| 2025-06-12 |    536.33   |   1172.22    |    0.0     |  375.67 |  0.0   |    55.73     |   0.0    |    0.0     |  867.55  |  0.0   |    0.0    |  194.93 |   472.27  |  2.12 |     0.0     |    0.0     |
| 2025-06-11 |    58.27    |    429.92    |    0.0     |   0.0   |  0.0   |    223.9     |   3.93   |    0.0     |  220.82  |  0.0   |   428.33  |  154.47 |   356.02  | 14.73 |     0.52    |    0.0     |
| 2025-06-09 |    531.8    |   1248.57    |    0.0     |  432.1  | 46.63  |    448.38    |   0.0    |    0.0     |  868.6   |  0.0   |   354.42  |   0.0   |   500.45  |  3.02 |     0.02    |    0.0     |
| 2025-06-08 |    388.95   |    1337.1    |    0.0     |  532.4  |  0.0   |    94.75     |   0.0    |    0.0     |  46.02   |  0.0   |    0.0    |   0.0   |    0.0    |  0.0  |     0.0     |    0.0     |
| 2025-06-07 |    307.85   |   1289.18    |    0.0     |  841.47 |  0.0   |     0.0      |   0.0    |    0.0     |  475.52  |  0.0   |    0.0    | 1272.62 |    0.0    |  0.0  |     0.0     |    0.0     |
| 2025-06-06 |    596.22   |    467.87    |    0.0     |  928.22 | 101.67 |    119.52    |   0.0    |    0.0     | 1067.55  |  0.0   |   222.67  | 1273.42 |    0.0    |  0.0  |     0.0     |    0.0     |
| 2025-06-05 |    681.97   |   1423.35    |   204.58   |  860.28 | 88.68  |    228.2     |   0.0    |    0.0     | 1067.77  |  0.0   |   814.2   |  556.23 |    0.0    |  0.0  |    153.1    |    0.0     |
| 2025-06-04 |    282.1    |   1372.17    |    0.0     |   0.0   |  25.3  |     0.0      |   0.0    |    0.0     |  627.7   |  0.0   |   911.03  |  630.15 |    0.0    |  0.0  |    217.17   |    0.0     |
| 2025-06-03 |    461.53   |   1423.38    |    0.0     |   0.0   |  0.0   |     0.0      |   0.0    |    0.0     |  858.97  |  0.0   |   631.77  |  130.93 |    0.0    |  0.0  |    166.07   |    0.0     |
| 2025-06-02 |    663.52   |    161.28    |    0.0     |   0.0   |  0.0   |     0.0      |   0.0    |    0.0     |  251.12  |  0.0   |    0.0    |   0.0   |    0.0    |  0.0  |     0.0     |    0.0     |
| 2025-06-01 |    632.93   |     0.68     |    0.0     |  169.27 |  0.0   |     0.0      |   0.0    |    0.0     |  141.57  |  0.0   |    0.0    |   0.0   |    0.0    |  0.0  |     0.0     |    0.0     |
| 2025-05-31 |    101.87   |     0.55     |    0.0     | 1066.13 |  0.0   |     0.0      |   0.0    |    0.0     |  105.6   |  0.0   |    0.0    |   0.0   |    0.0    |  0.0  |     0.0     |    0.0     |
| 2025-05-30 |    148.92   |    570.93    |   127.93   |  802.22 |  43.5  |     0.0      |   0.0    |    0.0     | 1069.93  |  0.0   |   530.48  |   0.0   |   165.08  |  0.0  |    139.0    |    0.0     |
| 2025-05-29 |    602.33   |    869.25    |    0.0     |   0.0   |  0.0   |     0.0      |   0.0    |    4.97    |  692.02  |  0.0   |   634.77  |  380.43 |   239.78  |  0.0  |    108.88   |    0.0     |
| 2025-05-28 |    608.73   |    763.42    |    0.0     |   0.0   | 172.6  |     0.0      |   0.0    |    0.0     |  746.85  |  0.0   |   367.2   |   0.0   |   28.97   |  0.0  |    71.47    |    0.0     |
| 2025-05-27 |    578.88   |    547.13    |    0.0     |   0.0   |  0.0   |    225.83    |   0.0    |    0.0     |  194.22  |  0.0   |  1389.87  | 1237.58 |    0.0    |  25.0 |     0.0     |    6.0     |
| 2025-05-26 |    276.82   |    400.88    |    0.0     |   0.0   |  0.0   |    419.62    |   0.0    |    0.0     |  491.17  |  0.0   |   607.12  |  78.42  |    0.0    |  0.0  |     0.0     |    0.0     |
| 2025-05-25 |    551.77   |   1145.48    |   222.18   |   0.0   |  0.0   |    239.12    |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    |  0.0  |     0.0     |    0.0     |
| 2025-05-24 |    630.75   |    891.53    |  1316.82   |  386.73 |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |   512.78  |   0.0   |    0.0    |  0.0  |     0.0     |    0.0     |
| 2025-05-23 |    198.03   |    726.1     |  1317.83   | 1384.22 |  0.0   |    246.85    |   0.0    |    0.0     |   0.0    |  0.0   |   677.12  |   0.0   |    0.0    |  0.0  |     0.0     |    0.0     |
| 2025-05-22 |    530.82   |   1224.23    |    0.0     |  679.3  | 90.33  |    200.03    |   0.0    |    0.0     |  295.0   |  0.0   |   176.47  |   0.0   |    0.0    |  0.0  |    174.15   |    0.0     |
| 2025-05-21 |    458.15   |    699.28    |    0.0     |  892.17 |  0.0   |     0.0      |   0.0    |   150.15   |   7.75   |  0.0   |   227.58  |  480.35 |   45.55   |  0.0  |    19.08    |    0.0     |
| 2025-05-20 |    518.77   |    872.23    |    0.0     |  880.95 | 96.25  |     0.0      |   0.0    |   265.1    |   8.68   |  0.0   |   899.13  |  405.45 |    0.0    |  0.0  |     0.0     |    0.0     |
| 2025-05-19 |    525.58   |   1323.85    |    0.0     |   0.0   | 30.08  |     0.0      |   0.0    |    0.0     |  52.62   |  0.0   |   605.1   |  433.93 |    0.0    |  0.0  |     0.0     |    0.0     |
| 2025-05-18 |    278.13   |    216.8     |   430.72   |   0.0   |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    |  0.0  |     0.0     |    0.0     |
| 2025-05-17 |    420.43   |    966.4     |   757.97   |   0.0   |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    |  0.0  |     0.0     |    0.0     |
| 2025-05-16 |    397.13   |    796.28    |   745.52   |   0.0   | 247.23 |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |   181.12  |   0.0   |    0.0    |  0.0  |     0.0     |    0.0     |
| 2025-05-15 |    663.3    |    926.62    |   680.45   |   0.0   |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |   312.47  |   0.0   |    0.0    |  0.0  |     0.0     |    0.0     |
| 2025-05-14 |    611.4    |   1049.63    |   684.9    |   0.0   |  0.0   |    16.25     |   0.0    |    0.0     |  15.17   |  0.0   |   249.57  |  1306.4 |    0.0    |  0.0  |     0.05    |    0.0     |
| 2025-05-13 |    428.08   |    851.9     |   685.35   |   0.0   | 212.02 |     0.0      |   0.0    |    0.0     |   0.0    | 309.67 |   484.43  |  295.02 |   314.58  |  6.03 |     0.0     |    0.0     |

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
