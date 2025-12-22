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
|  Total  |     213d    |     243d     |    50d     |  31d  |  66d  |     137d     |   56d    |    13d     |   172d   |  61d  |    141d   |   114d  |    73d    | 12d |     13d     |     4d     |  11d   |    23d     |
| 2025-12 |      21     |      22      |     5      |   0   |   16  |      12      |    13    |     0      |    17    |   10  |     16    |    5    |     1     |  0  |      0      |     0      |   0    |     2      |
| 2025-11 |      29     |      30      |     8      |   1   |   14  |      15      |    6     |     0      |    19    |   13  |     18    |    13   |     5     |  0  |      0      |     2      |   0    |     11     |
| 2025-10 |      25     |      31      |     5      |   0   |   5   |      16      |    1     |     0      |    21    |   12  |     18    |    14   |     2     |  0  |      0      |     0      |   0    |     0      |
| 2025-09 |      28     |      29      |     0      |   0   |   3   |      12      |    13    |     2      |    23    |   14  |     21    |    6    |     12    |  0  |      1      |     0      |   0    |     3      |
| 2025-08 |      12     |      29      |     1      |   0   |   0   |      23      |    0     |     5      |    25    |   0   |     6     |    14   |     15    |  0  |      1      |     0      |   0    |     2      |
| 2025-07 |      29     |      29      |     4      |   0   |   4   |      19      |    10    |     0      |    23    |   3   |     19    |    23   |     12    |  2  |      0      |     1      |   11   |     5      |
| 2025-06 |      28     |      28      |     3      |   8   |   6   |      20      |    10    |     0      |    26    |   6   |     11    |    18   |     15    |  7  |      5      |     0      |   0    |     0      |
| 2025-05 |      23     |      26      |     15     |   8   |   9   |      9       |    0     |     3      |    13    |   1   |     19    |    11   |     7     |  2  |      6      |     1      |   0    |     0      |
| 2025-04 |      18     |      19      |     9      |   14  |   9   |      11      |    3     |     3      |    5     |   2   |     13    |    10   |     4     |  1  |      0      |     0      |   0    |     0      |

## Daily login time in minutes for the past 30 days
|    date    | pengbenkang | yangjianchao | pengyinlun | juxin | hello  | shenjunzhong | fengjing | wangjianan | chendong |  hejun  | yangrenyu | xuezeyu | kangyuhan | lzd | yangjingkui | tangminjin | guohui | mashaocong |
|:----------:|:-----------:|:------------:|:----------:|:-----:|:------:|:------------:|:--------:|:----------:|:--------:|:-------:|:---------:|:-------:|:---------:|:---:|:-----------:|:----------:|:------:|:----------:|
|   Total    |    195.0h   |    413.6h    |   22.5h    |  0.0h | 52.2h  |    45.1h     |  105.7h  |    0.0h    |  233.3h  |  90.7h  |   247.2h  |  21.9h  |    0.2h   | 0.0h |     0.0h    |    0.0h    |  0.0h  |   34.8h    |
| 2025-12-22 |    443.67   |    810.05    |    86.6    |  0.0  | 190.33 |    241.33    |  266.57  |    0.0     |  493.77  |   2.85  |   880.42  |   0.0   |    9.42   | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-12-21 |    840.0    |    930.32    |    0.0     |  0.0  |  0.0   |    50.22     |   0.0    |    0.0     |   0.0    |   0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-12-20 |    800.05   |    367.2     |    0.0     |  0.0  |  0.0   |    70.57     |   0.0    |    0.0     |   0.0    |   0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-12-19 |    455.02   |    146.32    |    4.37    |  0.0  | 23.43  |    172.0     |   0.0    |    0.0     |  164.22  |   0.0   |   171.12  |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-12-18 |    676.9    |    807.7     |    0.0     |  0.0  | 109.32 |    429.92    |  523.22  |    0.0     |  366.7   |   0.0   |   904.33  |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-12-17 |    638.45   |   1051.22    |    0.0     |  0.0  | 219.3  |    175.62    |  821.12  |    0.0     |  608.6   |  10.75  |   893.52  |  103.48 |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-12-16 |    199.6    |    879.77    |   518.73   |  0.0  | 39.72  |    307.48    |  900.3   |    0.0     |  869.27  |  479.7  |   799.43  |  143.35 |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-12-15 |    256.15   |    977.68    |   149.85   |  0.0  | 294.0  |    154.82    |  141.83  |    0.0     |  825.05  |  697.37 |   777.97  |  545.38 |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-12-14 |    712.72   |    726.13    |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |  282.22  |  358.72 |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-12-13 |     0.0     |   1002.25    |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |   0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-12-12 |    117.37   |    837.68    |    0.0     |  0.0  | 57.55  |    131.0     |   0.0    |    0.0     |  601.07  |  380.93 |   463.52  |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-12-11 |    491.85   |    506.1     |    0.0     |  0.0  | 248.45 |    60.55     |  439.5   |    0.0     |  771.8   |  469.27 |   810.52  |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-12-10 |    335.52   |    814.67    |    0.0     |  0.0  | 122.28 |     0.0      |   0.0    |    0.0     |  515.67  |   0.0   |   921.22  |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-12-09 |    361.43   |    744.03    |    0.0     |  0.0  | 79.12  |     0.0      |  681.83  |    0.0     |  112.4   |   0.0   |   803.75  |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-12-08 |    486.63   |   1113.85    |    0.0     |  0.0  | 38.63  |     0.23     |  37.32   |    0.0     |  28.15   |   0.0   |   829.73  |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-12-07 |    839.8    |   1194.62    |    0.0     |  0.0  |  0.0   |     0.0      |  472.1   |    0.0     |   0.0    |   0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-12-06 |    68.97    |   1337.27    |    0.0     |  0.0  |  0.0   |     0.0      |  201.5   |    0.0     |   0.0    |   0.0   |    0.0    |  442.03 |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-12-05 |    201.93   |    934.23    |    0.0     |  0.0  | 37.47  |     0.0      |   0.0    |    0.0     |  686.9   |   0.0   |   841.4   |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-12-04 |    196.58   |    476.17    |    0.0     |  0.0  | 225.87 |     0.0      |  644.78  |    0.0     |  823.15  |  513.3  |   639.75  |  81.47  |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-12-03 |    336.48   |    568.73    |    0.0     |  0.0  | 241.78 |    101.63    |  368.58  |    0.0     |  858.47  | 1324.78 |   900.83  |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |  1364.35   |
| 2025-12-02 |    404.98   |   1311.92    |   48.78    |  0.0  | 97.42  |     0.0      |   0.0    |    0.0     |  823.15  |   0.0   |   806.82  |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |   719.27   |
| 2025-12-01 |    270.97   |    810.53    |    0.0     |  0.0  | 155.82 |     0.0      |  359.23  |    0.0     |  451.45  |  250.07 |   690.78  |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-11-30 |     0.0     |    601.5     |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |   0.15   |   0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-11-29 |    332.57   |   1212.75    |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |  675.75  |   0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    3.98    |
| 2025-11-28 |    243.95   |   1210.25    |    0.0     |  0.0  | 58.95  |     0.0      |   0.0    |    0.0     |  864.22  |  133.43 |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-11-27 |    195.45   |    953.23    |    0.0     |  0.0  | 236.72 |    417.73    |  485.83  |    0.0     |  880.95  |  510.22 |   514.27  |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-11-26 |    182.7    |   1206.18    |   110.27   |  0.07 | 154.88 |    318.95    |   0.0    |    0.0     |  873.18  |  138.43 |   791.58  |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-11-25 |    189.18   |    508.7     |   391.77   |  0.0  | 127.4  |    70.97     |   0.0    |    0.0     |  873.33  |  25.57  |   597.67  |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-11-24 |    785.85   |    773.0     |   41.23    |  0.0  | 371.67 |     0.0      |   0.0    |    0.0     |  547.82  |  149.05 |   791.77  |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.35    |
| 2025-11-23 |    636.45   |     0.87     |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |   0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |

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
