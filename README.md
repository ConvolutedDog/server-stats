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
|  Total  |     58d     |     62d      |    26d     |  30d  |  24d  |     31d      |    4d    |     6d     |   34d    |   3d  |    38d    |   33d   |    18d    |  6d |     11d     |     1d     |
| 2025-06 |      17     |      17      |     2      |   8   |   6   |      11      |    1     |     0      |    16    |   0   |     6     |    12   |     7     |  3  |      5      |     0      |
| 2025-05 |      23     |      26      |     15     |   8   |   9   |      9       |    0     |     3      |    13    |   1   |     19    |    11   |     7     |  2  |      6      |     1      |
| 2025-04 |      18     |      19      |     9      |   14  |   9   |      11      |    3     |     3      |    5     |   2   |     13    |    10   |     4     |  1  |      0      |     0      |

## Daily login time in minutes for the past 30 days
|    date    | pengbenkang | yangjianchao | pengyinlun |  juxin  | hello  | shenjunzhong | fengjing | wangjianan | chendong | hejun | yangrenyu | xuezeyu | kangyuhan |  lzd  | yangjingkui | tangminjin |
|:----------:|:-----------:|:------------:|:----------:|:-------:|:------:|:------------:|:--------:|:----------:|:--------:|:-----:|:---------:|:-------:|:---------:|:-----:|:-----------:|:----------:|
|   Total    |    230.7h   |    400.8h    |   53.2h    |  170.5h | 15.9h  |    65.0h     |   0.1h   |    7.0h    |  232.4h  |  0.0h |   166.5h  |  187.1h |   42.6h   |  0.7h |    17.5h    |    0.1h    |
| 2025-06-19 |    422.68   |    824.23    |    0.53    |   0.0   |  0.0   |    585.75    |   0.0    |    0.0     |  859.75  |  0.0  |    0.0    |  1229.6 |   192.45  |  0.0  |     0.0     |    0.0     |
| 2025-06-17 |    514.43   |    453.48    |    0.0     |   0.1   | 115.62 |    19.13     |   0.0    |    0.0     |  698.77  |  0.0  |    0.0    |  284.7  |   45.33   |  0.0  |     0.0     |    0.0     |
| 2025-06-16 |    571.23   |    703.55    |    0.0     |   0.0   | 142.45 |    239.93    |   0.0    |    0.0     |  860.1   |  0.0  |    0.0    |  352.77 |   288.93  |  0.0  |     0.0     |    0.0     |
| 2025-06-15 |    555.52   |     0.65     |    0.0     |   0.0   |  0.0   |     0.0      |   0.0    |    0.0     |  362.55  |  0.0  |    0.0    |   0.0   |    0.0    |  0.0  |     0.0     |    0.0     |
| 2025-06-14 |    574.1    |    968.6     |    0.0     |   0.0   |  0.0   |    63.62     |   0.0    |    0.0     |   0.0    |  0.0  |    0.0    | 1062.52 |    0.0    |  0.0  |     0.0     |    0.0     |
| 2025-06-13 |    331.57   |    735.62    |    0.0     |   0.0   |  0.0   |    487.53    |   0.0    |    0.0     | 1005.87  |  0.0  |    0.0    | 1065.68 |   222.33  |  0.0  |     0.0     |    0.0     |
| 2025-06-12 |    536.33   |   1172.22    |    0.0     |  375.67 |  0.0   |    55.73     |   0.0    |    0.0     |  867.55  |  0.0  |    0.0    |  194.93 |   472.27  |  2.12 |     0.0     |    0.0     |
| 2025-06-11 |    58.27    |    429.92    |    0.0     |   0.0   |  0.0   |    223.9     |   3.93   |    0.0     |  220.82  |  0.0  |   428.33  |  154.47 |   356.02  | 14.73 |     0.52    |    0.0     |
| 2025-06-09 |    531.8    |   1248.57    |    0.0     |  432.1  | 46.63  |    448.38    |   0.0    |    0.0     |  868.6   |  0.0  |   354.42  |   0.0   |   500.45  |  3.02 |     0.02    |    0.0     |
| 2025-06-08 |    388.95   |    1337.1    |    0.0     |  532.4  |  0.0   |    94.75     |   0.0    |    0.0     |  46.02   |  0.0  |    0.0    |   0.0   |    0.0    |  0.0  |     0.0     |    0.0     |
| 2025-06-07 |    307.85   |   1289.18    |    0.0     |  841.47 |  0.0   |     0.0      |   0.0    |    0.0     |  475.52  |  0.0  |    0.0    | 1272.62 |    0.0    |  0.0  |     0.0     |    0.0     |
| 2025-06-06 |    596.22   |    467.87    |    0.0     |  928.22 | 101.67 |    119.52    |   0.0    |    0.0     | 1067.55  |  0.0  |   222.67  | 1273.42 |    0.0    |  0.0  |     0.0     |    0.0     |
| 2025-06-05 |    681.97   |   1423.35    |   204.58   |  860.28 | 88.68  |    228.2     |   0.0    |    0.0     | 1067.77  |  0.0  |   814.2   |  556.23 |    0.0    |  0.0  |    153.1    |    0.0     |
| 2025-06-04 |    282.1    |   1372.17    |    0.0     |   0.0   |  25.3  |     0.0      |   0.0    |    0.0     |  627.7   |  0.0  |   911.03  |  630.15 |    0.0    |  0.0  |    217.17   |    0.0     |
| 2025-06-03 |    461.53   |   1423.38    |    0.0     |   0.0   |  0.0   |     0.0      |   0.0    |    0.0     |  858.97  |  0.0  |   631.77  |  130.93 |    0.0    |  0.0  |    166.07   |    0.0     |
| 2025-06-02 |    663.52   |    161.28    |    0.0     |   0.0   |  0.0   |     0.0      |   0.0    |    0.0     |  251.12  |  0.0  |    0.0    |   0.0   |    0.0    |  0.0  |     0.0     |    0.0     |
| 2025-06-01 |    632.93   |     0.68     |    0.0     |  169.27 |  0.0   |     0.0      |   0.0    |    0.0     |  141.57  |  0.0  |    0.0    |   0.0   |    0.0    |  0.0  |     0.0     |    0.0     |
| 2025-05-31 |    101.87   |     0.55     |    0.0     | 1066.13 |  0.0   |     0.0      |   0.0    |    0.0     |  105.6   |  0.0  |    0.0    |   0.0   |    0.0    |  0.0  |     0.0     |    0.0     |
| 2025-05-30 |    148.92   |    570.93    |   127.93   |  802.22 |  43.5  |     0.0      |   0.0    |    0.0     | 1069.93  |  0.0  |   530.48  |   0.0   |   165.08  |  0.0  |    139.0    |    0.0     |
| 2025-05-29 |    602.33   |    869.25    |    0.0     |   0.0   |  0.0   |     0.0      |   0.0    |    4.97    |  692.02  |  0.0  |   634.77  |  380.43 |   239.78  |  0.0  |    108.88   |    0.0     |
| 2025-05-28 |    608.73   |    763.42    |    0.0     |   0.0   | 172.6  |     0.0      |   0.0    |    0.0     |  746.85  |  0.0  |   367.2   |   0.0   |   28.97   |  0.0  |    71.47    |    0.0     |
| 2025-05-27 |    578.88   |    547.13    |    0.0     |   0.0   |  0.0   |    225.83    |   0.0    |    0.0     |  194.22  |  0.0  |  1389.87  | 1237.58 |    0.0    |  25.0 |     0.0     |    6.0     |
| 2025-05-26 |    276.82   |    400.88    |    0.0     |   0.0   |  0.0   |    419.62    |   0.0    |    0.0     |  491.17  |  0.0  |   607.12  |  78.42  |    0.0    |  0.0  |     0.0     |    0.0     |
| 2025-05-25 |    551.77   |   1145.48    |   222.18   |   0.0   |  0.0   |    239.12    |   0.0    |    0.0     |   0.0    |  0.0  |    0.0    |   0.0   |    0.0    |  0.0  |     0.0     |    0.0     |
| 2025-05-24 |    630.75   |    891.53    |  1316.82   |  386.73 |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0  |   512.78  |   0.0   |    0.0    |  0.0  |     0.0     |    0.0     |
| 2025-05-23 |    198.03   |    726.1     |  1317.83   | 1384.22 |  0.0   |    246.85    |   0.0    |    0.0     |   0.0    |  0.0  |   677.12  |   0.0   |    0.0    |  0.0  |     0.0     |    0.0     |
| 2025-05-22 |    530.82   |   1224.23    |    0.0     |  679.3  | 90.33  |    200.03    |   0.0    |    0.0     |  295.0   |  0.0  |   176.47  |   0.0   |    0.0    |  0.0  |    174.15   |    0.0     |
| 2025-05-21 |    458.15   |    699.28    |    0.0     |  892.17 |  0.0   |     0.0      |   0.0    |   150.15   |   7.75   |  0.0  |   227.58  |  480.35 |   45.55   |  0.0  |    19.08    |    0.0     |
| 2025-05-20 |    518.77   |    872.23    |    0.0     |  880.95 | 96.25  |     0.0      |   0.0    |   265.1    |   8.68   |  0.0  |   899.13  |  405.45 |    0.0    |  0.0  |     0.0     |    0.0     |
| 2025-05-19 |    525.58   |   1323.85    |    0.0     |   0.0   | 30.08  |     0.0      |   0.0    |    0.0     |  52.62   |  0.0  |   605.1   |  433.93 |    0.0    |  0.0  |     0.0     |    0.0     |

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
