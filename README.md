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
|  Total  |     62d     |     66d      |    26d     |  30d  |  24d  |     35d      |    7d    |     6d     |   38d    |   5d  |    39d    |   35d   |    20d    |  8d |     11d     |     1d     |
| 2025-06 |      21     |      21      |     2      |   8   |   6   |      15      |    4     |     0      |    20    |   2   |     7     |    14   |     9     |  5  |      5      |     0      |
| 2025-05 |      23     |      26      |     15     |   8   |   9   |      9       |    0     |     3      |    13    |   1   |     19    |    11   |     7     |  2  |      6      |     1      |
| 2025-04 |      18     |      19      |     9      |   14  |   9   |      11      |    3     |     3      |    5     |   2   |     13    |    10   |     4     |  1  |      0      |     0      |

## Daily login time in minutes for the past 30 days
|    date    | pengbenkang | yangjianchao | pengyinlun |  juxin  | hello  | shenjunzhong | fengjing | wangjianan | chendong | hejun | yangrenyu | xuezeyu | kangyuhan |  lzd   | yangjingkui | tangminjin |
|:----------:|:-----------:|:------------:|:----------:|:-------:|:------:|:------------:|:--------:|:----------:|:--------:|:-----:|:---------:|:-------:|:---------:|:------:|:-----------:|:----------:|
|   Total    |    226.2h   |    371.8h    |   53.2h    |  129.6h | 12.3h  |    87.9h     |  21.5h   |    0.1h    |  281.6h  |  1.5h |   138.7h  |  195.5h |   45.4h   |  7.0h  |    14.3h    |    0.1h    |
| 2025-06-24 |    480.82   |   1152.25    |    0.0     |   0.0   |  0.0   |    506.83    |  940.7   |    0.0     | 1338.83  |  2.45 |    0.0    |  941.5  |    0.0    | 33.07  |     0.0     |    0.0     |
| 2025-06-23 |    572.07   |    850.78    |    0.0     |   0.0   |  0.0   |    456.68    |  126.88  |    0.0     |  865.28  | 86.28 |   240.97  |  884.17 |   172.42  | 342.73 |     0.0     |    0.0     |
| 2025-06-21 |    335.78   |     0.62     |    0.0     |   0.0   |  0.0   |    282.28    |  218.58  |    0.0     |  346.4   |  0.0  |    0.0    |   0.0   |    0.0    |  0.0   |     0.0     |    0.0     |
| 2025-06-20 |    372.53   |    375.5     |    0.0     |   0.0   |  0.0   |    333.17    |   0.0    |    0.0     |  767.87  |  0.0  |    0.0    |   0.0   |   40.13   |  0.0   |     0.0     |    0.0     |
| 2025-06-19 |    422.68   |    824.23    |    0.53    |   0.0   |  0.0   |    585.75    |   0.0    |    0.0     |  859.75  |  0.0  |    0.0    |  1229.6 |   192.45  |  0.0   |     0.0     |    0.0     |
| 2025-06-17 |    514.43   |    453.48    |    0.0     |   0.1   | 115.62 |    19.13     |   0.0    |    0.0     |  698.77  |  0.0  |    0.0    |  284.7  |   45.33   |  0.0   |     0.0     |    0.0     |
| 2025-06-16 |    571.23   |    703.55    |    0.0     |   0.0   | 142.45 |    239.93    |   0.0    |    0.0     |  860.1   |  0.0  |    0.0    |  352.77 |   288.93  |  0.0   |     0.0     |    0.0     |
| 2025-06-15 |    555.52   |     0.65     |    0.0     |   0.0   |  0.0   |     0.0      |   0.0    |    0.0     |  362.55  |  0.0  |    0.0    |   0.0   |    0.0    |  0.0   |     0.0     |    0.0     |
| 2025-06-14 |    574.1    |    968.6     |    0.0     |   0.0   |  0.0   |    63.62     |   0.0    |    0.0     |   0.0    |  0.0  |    0.0    | 1062.52 |    0.0    |  0.0   |     0.0     |    0.0     |
| 2025-06-13 |    331.57   |    735.62    |    0.0     |   0.0   |  0.0   |    487.53    |   0.0    |    0.0     | 1005.87  |  0.0  |    0.0    | 1065.68 |   222.33  |  0.0   |     0.0     |    0.0     |
| 2025-06-12 |    536.33   |   1172.22    |    0.0     |  375.67 |  0.0   |    55.73     |   0.0    |    0.0     |  867.55  |  0.0  |    0.0    |  194.93 |   472.27  |  2.12  |     0.0     |    0.0     |
| 2025-06-11 |    58.27    |    429.92    |    0.0     |   0.0   |  0.0   |    223.9     |   3.93   |    0.0     |  220.82  |  0.0  |   428.33  |  154.47 |   356.02  | 14.73  |     0.52    |    0.0     |
| 2025-06-09 |    531.8    |   1248.57    |    0.0     |  432.1  | 46.63  |    448.38    |   0.0    |    0.0     |  868.6   |  0.0  |   354.42  |   0.0   |   500.45  |  3.02  |     0.02    |    0.0     |
| 2025-06-08 |    388.95   |    1337.1    |    0.0     |  532.4  |  0.0   |    94.75     |   0.0    |    0.0     |  46.02   |  0.0  |    0.0    |   0.0   |    0.0    |  0.0   |     0.0     |    0.0     |
| 2025-06-07 |    307.85   |   1289.18    |    0.0     |  841.47 |  0.0   |     0.0      |   0.0    |    0.0     |  475.52  |  0.0  |    0.0    | 1272.62 |    0.0    |  0.0   |     0.0     |    0.0     |
| 2025-06-06 |    596.22   |    467.87    |    0.0     |  928.22 | 101.67 |    119.52    |   0.0    |    0.0     | 1067.55  |  0.0  |   222.67  | 1273.42 |    0.0    |  0.0   |     0.0     |    0.0     |
| 2025-06-05 |    681.97   |   1423.35    |   204.58   |  860.28 | 88.68  |    228.2     |   0.0    |    0.0     | 1067.77  |  0.0  |   814.2   |  556.23 |    0.0    |  0.0   |    153.1    |    0.0     |
| 2025-06-04 |    282.1    |   1372.17    |    0.0     |   0.0   |  25.3  |     0.0      |   0.0    |    0.0     |  627.7   |  0.0  |   911.03  |  630.15 |    0.0    |  0.0   |    217.17   |    0.0     |
| 2025-06-03 |    461.53   |   1423.38    |    0.0     |   0.0   |  0.0   |     0.0      |   0.0    |    0.0     |  858.97  |  0.0  |   631.77  |  130.93 |    0.0    |  0.0   |    166.07   |    0.0     |
| 2025-06-02 |    663.52   |    161.28    |    0.0     |   0.0   |  0.0   |     0.0      |   0.0    |    0.0     |  251.12  |  0.0  |    0.0    |   0.0   |    0.0    |  0.0   |     0.0     |    0.0     |
| 2025-06-01 |    632.93   |     0.68     |    0.0     |  169.27 |  0.0   |     0.0      |   0.0    |    0.0     |  141.57  |  0.0  |    0.0    |   0.0   |    0.0    |  0.0   |     0.0     |    0.0     |
| 2025-05-31 |    101.87   |     0.55     |    0.0     | 1066.13 |  0.0   |     0.0      |   0.0    |    0.0     |  105.6   |  0.0  |    0.0    |   0.0   |    0.0    |  0.0   |     0.0     |    0.0     |
| 2025-05-30 |    148.92   |    570.93    |   127.93   |  802.22 |  43.5  |     0.0      |   0.0    |    0.0     | 1069.93  |  0.0  |   530.48  |   0.0   |   165.08  |  0.0   |    139.0    |    0.0     |
| 2025-05-29 |    602.33   |    869.25    |    0.0     |   0.0   |  0.0   |     0.0      |   0.0    |    4.97    |  692.02  |  0.0  |   634.77  |  380.43 |   239.78  |  0.0   |    108.88   |    0.0     |
| 2025-05-28 |    608.73   |    763.42    |    0.0     |   0.0   | 172.6  |     0.0      |   0.0    |    0.0     |  746.85  |  0.0  |   367.2   |   0.0   |   28.97   |  0.0   |    71.47    |    0.0     |
| 2025-05-27 |    578.88   |    547.13    |    0.0     |   0.0   |  0.0   |    225.83    |   0.0    |    0.0     |  194.22  |  0.0  |  1389.87  | 1237.58 |    0.0    |  25.0  |     0.0     |    6.0     |
| 2025-05-26 |    276.82   |    400.88    |    0.0     |   0.0   |  0.0   |    419.62    |   0.0    |    0.0     |  491.17  |  0.0  |   607.12  |  78.42  |    0.0    |  0.0   |     0.0     |    0.0     |
| 2025-05-25 |    551.77   |   1145.48    |   222.18   |   0.0   |  0.0   |    239.12    |   0.0    |    0.0     |   0.0    |  0.0  |    0.0    |   0.0   |    0.0    |  0.0   |     0.0     |    0.0     |
| 2025-05-24 |    630.75   |    891.53    |  1316.82   |  386.73 |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0  |   512.78  |   0.0   |    0.0    |  0.0   |     0.0     |    0.0     |
| 2025-05-23 |    198.03   |    726.1     |  1317.83   | 1384.22 |  0.0   |    246.85    |   0.0    |    0.0     |   0.0    |  0.0  |   677.12  |   0.0   |    0.0    |  0.0   |     0.0     |    0.0     |

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
