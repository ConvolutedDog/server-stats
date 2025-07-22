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
|  month  | pengbenkang | yangjianchao | pengyinlun | juxin | hello | shenjunzhong | fengjing | wangjianan | chendong | hejun | yangrenyu | xuezeyu | kangyuhan | lzd | yangjingkui | tangminjin | guohui | mashaocong |
|:-------:|:-----------:|:------------:|:----------:|:-----:|:-----:|:------------:|:--------:|:----------:|:--------:|:-----:|:---------:|:-------:|:---------:|:---:|:-----------:|:----------:|:------:|:----------:|
|  Total  |     90d     |     94d      |    30d     |  30d  |  28d  |     52d      |   17d    |     6d     |   60d    |  11d  |    58d    |   56d   |    36d    | 12d |     11d     |     2d     |  11d   |     4d     |
| 2025-07 |      21     |      21      |     3      |   0   |   4   |      12      |    4     |     0      |    16    |   2   |     15    |    17   |     10    |  2  |      0      |     1      |   11   |     4      |
| 2025-06 |      28     |      28      |     3      |   8   |   6   |      20      |    10    |     0      |    26    |   6   |     11    |    18   |     15    |  7  |      5      |     0      |   0    |     0      |
| 2025-05 |      23     |      26      |     15     |   8   |   9   |      9       |    0     |     3      |    13    |   1   |     19    |    11   |     7     |  2  |      6      |     1      |   0    |     0      |
| 2025-04 |      18     |      19      |     9      |   14  |   9   |      11      |    3     |     3      |    5     |   2   |     13    |    10   |     4     |  1  |      0      |     0      |   0    |     0      |

## Daily login time in minutes for the past 30 days
|    date    | pengbenkang | yangjianchao | pengyinlun | juxin | hello  | shenjunzhong | fengjing | wangjianan | chendong | hejun  | yangrenyu | xuezeyu | kangyuhan |  lzd   | yangjingkui | tangminjin | guohui | mashaocong |
|:----------:|:-----------:|:------------:|:----------:|:-----:|:------:|:------------:|:--------:|:----------:|:--------:|:------:|:---------:|:-------:|:---------:|:------:|:-----------:|:----------:|:------:|:----------:|
|   Total    |    229.2h   |    415.7h    |    4.0h    |  0.0h |  8.7h  |    103.3h    |  142.9h  |    0.0h    |  235.5h  | 39.8h  |   156.8h  |  192.4h |   72.5h   | 10.0h  |     0.0h    |    0.0h    | 24.6h  |   10.6h    |
| 2025-07-22 |    606.62   |    780.88    |   115.05   |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |  755.22  |  0.0   |   574.53  |  349.28 |    0.0    | 118.2  |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-07-21 |    474.17   |    575.73    |   102.28   |  0.0  | 113.3  |    485.27    |   0.0    |    0.0     |  446.02  |  0.0   |   560.98  |  138.08 |    0.0    | 102.73 |     0.0     |    0.0     | 81.72  |    2.45    |
| 2025-07-20 |    589.58   |    100.53    |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    |  0.0   |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-07-18 |    521.57   |    766.67    |    0.0     |  0.0  | 28.35  |    257.73    |   0.0    |    0.0     |  159.97  |  0.0   |   240.45  |   0.0   |    0.0    |  0.0   |     0.0     |    0.0     | 98.28  |    0.0     |
| 2025-07-17 |    885.9    |    985.83    |    0.0     |  0.0  |  0.0   |    112.05    |   0.0    |    0.0     |  384.22  |  0.0   |   650.83  |  114.43 |    0.0    |  0.0   |     0.0     |    0.0     | 63.13  |    3.95    |
| 2025-07-16 |    435.7    |   1132.87    |    0.0     |  0.0  |  0.0   |     0.0      |  884.7   |    0.0     |  307.02  |  0.0   |   657.7   |  206.35 |   242.62  |  0.0   |     0.0     |    0.0     | 260.98 |    1.45    |
| 2025-07-15 |    426.05   |    888.05    |    0.0     |  0.0  | 153.17 |    317.6     | 1077.43  |    0.0     |   0.0    |  0.0   |   579.2   | 1016.02 |   310.07  |  0.0   |     0.0     |    0.0     | 182.27 |   627.07   |
| 2025-07-14 |    616.02   |    1000.6    |    0.0     |  0.0  | 228.67 |    523.27    |  937.9   |    0.0     |  858.72  |  0.0   |   588.13  |  319.4  |   352.05  |  0.0   |     0.0     |    0.0     | 108.55 |    0.0     |
| 2025-07-13 |    59.98    |   1168.85    |    0.0     |  0.0  |  0.0   |    290.43    |   0.0    |    0.0     |   1.87   |  0.0   |    0.0    |   0.0   |    0.0    |  0.0   |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-07-12 |    95.77    |   1091.52    |    0.0     |  0.0  |  0.0   |    210.9     |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |  288.58 |    0.0    |  0.0   |     0.0     |    0.73    |  0.0   |    0.0     |
| 2025-07-11 |    278.9    |   1369.42    |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |  575.2   |  0.0   |   158.08  |  493.25 |   103.52  |  0.0   |     0.0     |    0.0     | 162.87 |    0.0     |
| 2025-07-10 |    456.18   |   1269.08    |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |  323.05  |  0.0   |   648.78  |  560.67 |   378.37  |  0.0   |     0.0     |    0.0     | 210.12 |    0.0     |
| 2025-07-09 |    532.0    |   1268.48    |    0.0     |  0.0  |  0.0   |    350.52    |   0.0    |    0.0     |  426.4   |  0.0   |   675.97  |  305.47 |   286.48  |  0.0   |     0.0     |    0.0     | 193.72 |    0.0     |
| 2025-07-08 |    704.82   |   1010.88    |    0.0     |  0.0  |  0.0   |    452.92    |   0.0    |    0.0     |  363.58  |  0.0   |   615.75  |  196.27 |   82.88   |  0.0   |     0.0     |    0.0     |  8.03  |    0.0     |
| 2025-07-07 |    494.02   |    1278.7    |    0.0     |  0.0  |  0.0   |    431.07    |   0.0    |    0.0     |  177.5   |  0.0   |   261.75  |  324.95 |   43.98   |  0.0   |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-07-06 |    455.73   |   1068.02    |    0.0     |  0.0  |  0.0   |    315.83    |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    |  0.0   |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-07-05 |    134.93   |    525.37    |    0.0     |  0.0  |  0.0   |    265.63    |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    | 1138.55 |    0.0    |  0.0   |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-07-04 |    270.68   |    204.37    |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |  222.43  |  0.0   |   163.0   | 1331.82 |    0.0    |  0.0   |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-07-03 |    224.17   |    484.42    |    0.88    |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |  609.48  |  0.0   |    0.0    | 1270.75 |    0.0    |  0.0   |     0.0     |    0.0     | 105.82 |    0.0     |
| 2025-07-02 |    559.33   |    31.45     |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |  519.17  | 295.62 |   312.43  |  411.07 |   419.37  |  0.0   |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-07-01 |    626.2    |    841.95    |    0.0     |  0.0  |  0.0   |     0.0      |  813.22  |    0.0     |  548.83  | 854.45 |   565.73  |  333.87 |   773.25  |  0.0   |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-06-30 |    486.8    |    317.85    |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |  864.33  | 294.75 |   546.3   |  159.48 |   453.78  |  0.0   |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-06-29 |    529.18   |    661.9     |    0.0     |  0.0  |  0.0   |     0.0      |  858.6   |    0.0     |   0.0    | 727.5  |    0.0    |  222.75 |   34.03   |  2.97  |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-06-28 |    448.98   |   1067.52    |    0.0     |  0.0  |  0.0   |    269.83    |  880.25  |    0.0     |  666.7   |  0.0   |    0.0    |   0.0   |   150.98  |  0.63  |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-06-27 |    213.02   |   1389.88    |    0.0     |  0.0  |  0.0   |    149.77    |  814.05  |    0.0     |  839.13  | 125.78 |   196.07  |   0.0   |   207.42  |  0.0   |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-06-26 |    321.52   |    710.42    |    0.0     |  0.0  |  0.0   |    146.97    |  673.23  |    0.0     | 1034.98  |  2.8   |   487.5   |  324.87 |   144.72  |  0.0   |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-06-25 |    577.65   |    949.97    |    23.6    |  0.0  |  0.0   |    323.23    |  195.18  |    0.0     |  1188.9  |  0.0   |   682.1   |  213.38 |   193.02  |  0.0   |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-06-24 |    480.82   |   1152.25    |    0.0     |  0.0  |  0.0   |    506.83    |  940.7   |    0.0     | 1338.83  |  2.45  |    0.0    |  941.5  |    0.0    | 33.07  |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-06-23 |    572.07   |    850.78    |    0.0     |  0.0  |  0.0   |    456.68    |  126.88  |    0.0     |  865.28  | 86.28  |   240.97  |  884.17 |   172.42  | 342.73 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-06-22 |    671.42   |     0.67     |    0.0     |  0.0  |  0.0   |    330.07    |  374.48  |    0.0     |  653.72  |  0.0   |    0.0    |   0.0   |    0.0    |  0.0   |     0.0     |    0.0     |  0.0   |    0.0     |

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
