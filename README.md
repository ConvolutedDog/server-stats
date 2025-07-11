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
|  month  | pengbenkang | yangjianchao | pengyinlun | juxin | hello | shenjunzhong | fengjing | wangjianan | chendong | hejun | yangrenyu | xuezeyu | kangyuhan | lzd | yangjingkui | tangminjin | guohui |
|:-------:|:-----------:|:------------:|:----------:|:-----:|:-----:|:------------:|:--------:|:----------:|:--------:|:-----:|:---------:|:-------:|:---------:|:---:|:-----------:|:----------:|:------:|
|  Total  |     81d     |     85d      |    28d     |  30d  |  24d  |     46d      |   14d    |     6d     |   53d    |  11d  |    51d    |   50d   |    33d    | 10d |     11d     |     2d     |   5d   |
| 2025-07 |      12     |      12      |     1      |   0   |   0   |      6       |    1     |     0      |    9     |   2   |     8     |    11   |     7     |  0  |      0      |     1      |   5    |
| 2025-06 |      28     |      28      |     3      |   8   |   6   |      20      |    10    |     0      |    26    |   6   |     11    |    18   |     15    |  7  |      5      |     0      |   0    |
| 2025-05 |      23     |      26      |     15     |   8   |   9   |      9       |    0     |     3      |    13    |   1   |     19    |    11   |     7     |  2  |      6      |     1      |   0    |
| 2025-04 |      18     |      19      |     9      |   14  |   9   |      11      |    3     |     3      |    5     |   2   |     13    |    10   |     4     |  1  |      0      |     0      |   0    |

## Daily login time in minutes for the past 30 days
|    date    | pengbenkang | yangjianchao | pengyinlun | juxin  | hello  | shenjunzhong | fengjing | wangjianan | chendong | hejun  | yangrenyu | xuezeyu | kangyuhan |  lzd   | yangjingkui | tangminjin | guohui |
|:----------:|:-----------:|:------------:|:----------:|:------:|:------:|:------------:|:--------:|:----------:|:--------:|:------:|:---------:|:-------:|:---------:|:------:|:-----------:|:----------:|:------:|
|   Total    |    222.5h   |    379.7h    |    0.4h    |  6.3h  |  4.3h  |    104.6h    |  98.3h   |    0.0h    |  283.1h  | 39.8h  |   92.6h   |  226.5h |   78.4h   |  6.4h  |     0.0h    |    0.0h    | 11.3h  |
| 2025-07-12 |    95.77    |   1091.52    |    0.0     |  0.0   |  0.0   |    210.9     |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |  288.58 |    0.0    |  0.0   |     0.0     |    0.73    |  0.0   |
| 2025-07-11 |    278.9    |   1369.42    |    0.0     |  0.0   |  0.0   |     0.0      |   0.0    |    0.0     |  575.2   |  0.0   |   158.08  |  493.25 |   103.52  |  0.0   |     0.0     |    0.0     | 162.87 |
| 2025-07-10 |    456.18   |   1269.08    |    0.0     |  0.0   |  0.0   |     0.0      |   0.0    |    0.0     |  323.05  |  0.0   |   648.78  |  560.67 |   378.37  |  0.0   |     0.0     |    0.0     | 210.12 |
| 2025-07-09 |    532.0    |   1268.48    |    0.0     |  0.0   |  0.0   |    350.52    |   0.0    |    0.0     |  426.4   |  0.0   |   675.97  |  305.47 |   286.48  |  0.0   |     0.0     |    0.0     | 193.72 |
| 2025-07-08 |    704.82   |   1010.88    |    0.0     |  0.0   |  0.0   |    452.92    |   0.0    |    0.0     |  363.58  |  0.0   |   615.75  |  196.27 |   82.88   |  0.0   |     0.0     |    0.0     |  8.03  |
| 2025-07-07 |    494.02   |    1278.7    |    0.0     |  0.0   |  0.0   |    431.07    |   0.0    |    0.0     |  177.5   |  0.0   |   261.75  |  324.95 |   43.98   |  0.0   |     0.0     |    0.0     |  0.0   |
| 2025-07-06 |    455.73   |   1068.02    |    0.0     |  0.0   |  0.0   |    315.83    |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    |  0.0   |     0.0     |    0.0     |  0.0   |
| 2025-07-05 |    134.93   |    525.37    |    0.0     |  0.0   |  0.0   |    265.63    |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    | 1138.55 |    0.0    |  0.0   |     0.0     |    0.0     |  0.0   |
| 2025-07-04 |    270.68   |    204.37    |    0.0     |  0.0   |  0.0   |     0.0      |   0.0    |    0.0     |  222.43  |  0.0   |   163.0   | 1331.82 |    0.0    |  0.0   |     0.0     |    0.0     |  0.0   |
| 2025-07-03 |    224.17   |    484.42    |    0.88    |  0.0   |  0.0   |     0.0      |   0.0    |    0.0     |  609.48  |  0.0   |    0.0    | 1270.75 |    0.0    |  0.0   |     0.0     |    0.0     | 105.82 |
| 2025-07-02 |    559.33   |    31.45     |    0.0     |  0.0   |  0.0   |     0.0      |   0.0    |    0.0     |  519.17  | 295.62 |   312.43  |  411.07 |   419.37  |  0.0   |     0.0     |    0.0     |  0.0   |
| 2025-07-01 |    626.2    |    841.95    |    0.0     |  0.0   |  0.0   |     0.0      |  813.22  |    0.0     |  548.83  | 854.45 |   565.73  |  333.87 |   773.25  |  0.0   |     0.0     |    0.0     |  0.0   |
| 2025-06-30 |    486.8    |    317.85    |    0.0     |  0.0   |  0.0   |     0.0      |   0.0    |    0.0     |  864.33  | 294.75 |   546.3   |  159.48 |   453.78  |  0.0   |     0.0     |    0.0     |  0.0   |
| 2025-06-29 |    529.18   |    661.9     |    0.0     |  0.0   |  0.0   |     0.0      |  858.6   |    0.0     |   0.0    | 727.5  |    0.0    |  222.75 |   34.03   |  2.97  |     0.0     |    0.0     |  0.0   |
| 2025-06-28 |    448.98   |   1067.52    |    0.0     |  0.0   |  0.0   |    269.83    |  880.25  |    0.0     |  666.7   |  0.0   |    0.0    |   0.0   |   150.98  |  0.63  |     0.0     |    0.0     |  0.0   |
| 2025-06-27 |    213.02   |   1389.88    |    0.0     |  0.0   |  0.0   |    149.77    |  814.05  |    0.0     |  839.13  | 125.78 |   196.07  |   0.0   |   207.42  |  0.0   |     0.0     |    0.0     |  0.0   |
| 2025-06-26 |    321.52   |    710.42    |    0.0     |  0.0   |  0.0   |    146.97    |  673.23  |    0.0     | 1034.98  |  2.8   |   487.5   |  324.87 |   144.72  |  0.0   |     0.0     |    0.0     |  0.0   |
| 2025-06-25 |    577.65   |    949.97    |    23.6    |  0.0   |  0.0   |    323.23    |  195.18  |    0.0     |  1188.9  |  0.0   |   682.1   |  213.38 |   193.02  |  0.0   |     0.0     |    0.0     |  0.0   |
| 2025-06-24 |    480.82   |   1152.25    |    0.0     |  0.0   |  0.0   |    506.83    |  940.7   |    0.0     | 1338.83  |  2.45  |    0.0    |  941.5  |    0.0    | 33.07  |     0.0     |    0.0     |  0.0   |
| 2025-06-23 |    572.07   |    850.78    |    0.0     |  0.0   |  0.0   |    456.68    |  126.88  |    0.0     |  865.28  | 86.28  |   240.97  |  884.17 |   172.42  | 342.73 |     0.0     |    0.0     |  0.0   |
| 2025-06-22 |    671.42   |     0.67     |    0.0     |  0.0   |  0.0   |    330.07    |  374.48  |    0.0     |  653.72  |  0.0   |    0.0    |   0.0   |    0.0    |  0.0   |     0.0     |    0.0     |  0.0   |
| 2025-06-21 |    335.78   |     0.62     |    0.0     |  0.0   |  0.0   |    282.28    |  218.58  |    0.0     |  346.4   |  0.0   |    0.0    |   0.0   |    0.0    |  0.0   |     0.0     |    0.0     |  0.0   |
| 2025-06-20 |    372.53   |    375.5     |    0.0     |  0.0   |  0.0   |    333.17    |   0.0    |    0.0     |  767.87  |  0.0   |    0.0    |   0.0   |   40.13   |  0.0   |     0.0     |    0.0     |  0.0   |
| 2025-06-19 |    422.68   |    824.23    |    0.53    |  0.0   |  0.0   |    585.75    |   0.0    |    0.0     |  859.75  |  0.0   |    0.0    |  1229.6 |   192.45  |  0.0   |     0.0     |    0.0     |  0.0   |
| 2025-06-17 |    514.43   |    453.48    |    0.0     |  0.1   | 115.62 |    19.13     |   0.0    |    0.0     |  698.77  |  0.0   |    0.0    |  284.7  |   45.33   |  0.0   |     0.0     |    0.0     |  0.0   |
| 2025-06-16 |    571.23   |    703.55    |    0.0     |  0.0   | 142.45 |    239.93    |   0.0    |    0.0     |  860.1   |  0.0   |    0.0    |  352.77 |   288.93  |  0.0   |     0.0     |    0.0     |  0.0   |
| 2025-06-15 |    555.52   |     0.65     |    0.0     |  0.0   |  0.0   |     0.0      |   0.0    |    0.0     |  362.55  |  0.0   |    0.0    |   0.0   |    0.0    |  0.0   |     0.0     |    0.0     |  0.0   |
| 2025-06-14 |    574.1    |    968.6     |    0.0     |  0.0   |  0.0   |    63.62     |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    | 1062.52 |    0.0    |  0.0   |     0.0     |    0.0     |  0.0   |
| 2025-06-13 |    331.57   |    735.62    |    0.0     |  0.0   |  0.0   |    487.53    |   0.0    |    0.0     | 1005.87  |  0.0   |    0.0    | 1065.68 |   222.33  |  0.0   |     0.0     |    0.0     |  0.0   |
| 2025-06-12 |    536.33   |   1172.22    |    0.0     | 375.67 |  0.0   |    55.73     |   0.0    |    0.0     |  867.55  |  0.0   |    0.0    |  194.93 |   472.27  |  2.12  |     0.0     |    0.0     |  0.0   |

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
