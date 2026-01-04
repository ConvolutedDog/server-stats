# SSH Session Time Report (Daily/Monthly Automation)

<div align="center">
  <a href="https://convoluteddog.github.io/server-stats/" target="_blank">
    <img src="https://github.com/ConvolutedDog/server-stats/blob/main/dashboard/example.png" alt="SSH Dashboard" width="85%" style="border-radius: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.15); border: 1px solid #e1e4e8; cursor: pointer;">
  </a>
  <br>
  <em>Click image to view interactive dashboard 🔗</em>
</div>

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
|  Total  |     220d    |     251d     |    53d     |  31d  |  71d  |     143d     |   62d    |    13d     |   179d   |  65d  |    147d   |   114d  |    74d    | 12d |     13d     |     4d     |  11d   |    24d     |
| 2026-01 |      1      |      1       |     0      |   0   |   0   |      0       |    0     |     0      |    0     |   0   |     0     |    0    |     0     |  0  |      0      |     0      |   0    |     0      |
| 2025-12 |      27     |      29      |     8      |   0   |   21  |      18      |    19    |     0      |    24    |   14  |     22    |    5    |     2     |  0  |      0      |     0      |   0    |     3      |
| 2025-11 |      29     |      30      |     8      |   1   |   14  |      15      |    6     |     0      |    19    |   13  |     18    |    13   |     5     |  0  |      0      |     2      |   0    |     11     |
| 2025-10 |      25     |      31      |     5      |   0   |   5   |      16      |    1     |     0      |    21    |   12  |     18    |    14   |     2     |  0  |      0      |     0      |   0    |     0      |
| 2025-09 |      28     |      29      |     0      |   0   |   3   |      12      |    13    |     2      |    23    |   14  |     21    |    6    |     12    |  0  |      1      |     0      |   0    |     3      |
| 2025-08 |      12     |      29      |     1      |   0   |   0   |      23      |    0     |     5      |    25    |   0   |     6     |    14   |     15    |  0  |      1      |     0      |   0    |     2      |
| 2025-07 |      29     |      29      |     4      |   0   |   4   |      19      |    10    |     0      |    23    |   3   |     19    |    23   |     12    |  2  |      0      |     1      |   11   |     5      |
| 2025-06 |      28     |      28      |     3      |   8   |   6   |      20      |    10    |     0      |    26    |   6   |     11    |    18   |     15    |  7  |      5      |     0      |   0    |     0      |
| 2025-05 |      23     |      26      |     15     |   8   |   9   |      9       |    0     |     3      |    13    |   1   |     19    |    11   |     7     |  2  |      6      |     1      |   0    |     0      |
| 2025-04 |      18     |      19      |     9      |   14  |   9   |      11      |    3     |     3      |    5     |   2   |     13    |    10   |     4     |  1  |      0      |     0      |   0    |     0      |

## Daily login time in minutes for the past 30 days
|    date    | pengbenkang | yangjianchao | pengyinlun | juxin | hello  | shenjunzhong | fengjing | wangjianan | chendong | hejun  | yangrenyu | xuezeyu | kangyuhan | lzd | yangjingkui | tangminjin | guohui | mashaocong |
|:----------:|:-----------:|:------------:|:----------:|:-----:|:------:|:------------:|:--------:|:----------:|:--------:|:------:|:---------:|:-------:|:---------:|:---:|:-----------:|:----------:|:------:|:----------:|
|   Total    |    173.7h   |    370.5h    |   27.0h    |  0.0h | 44.2h  |    44.8h     |  133.5h  |    0.0h    |  178.4h  | 69.9h  |   221.4h  |  20.6h  |    0.3h   | 0.0h |     0.0h    |    0.0h    |  0.0h  |    6.0h    |
| 2026-01-03 |     0.0     |     0.0      |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2026-01-02 |     0.0     |     0.0      |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2026-01-01 |    135.5    |     0.82     |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-12-31 |     0.0     |     0.0      |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-12-30 |    158.45   |    693.6     |   307.22   |  0.0  | 230.2  |    218.43    |  909.82  |    0.0     | 1379.92  | 71.65  |   452.7   |   0.0   |    6.35   | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-12-29 |    194.37   |    791.12    |   177.28   |  0.0  | 165.45 |    119.35    |  787.65  |    0.0     |  459.02  | 685.7  |   766.3   |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |   361.2    |
| 2025-12-28 |     0.0     |     0.0      |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-12-27 |    400.3    |    854.68    |    0.0     |  0.0  |  0.0   |    103.08    |  837.37  |    0.0     |  659.52  |  0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-12-26 |     0.0     |   1130.73    |    0.0     |  0.0  |  0.0   |     0.0      |  492.08  |    0.0     |  319.3   | 734.62 |   420.18  |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-12-25 |    506.13   |   1360.97    |    0.0     |  0.0  | 326.22 |    56.22     |  132.58  |    0.0     |  25.05   | 302.68 |   903.42  |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-12-24 |    657.08   |    889.5     |    0.0     |  0.0  | 363.22 |    49.08     |  366.33  |    0.0     |  813.47  |  0.0   |   831.62  |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-12-23 |    441.63   |   1329.95    |   376.83   |  0.0  | 105.13 |    346.43    |   0.0    |    0.0     |  724.77  |  0.0   |   815.45  |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-12-22 |    443.67   |    810.05    |    86.6    |  0.0  | 190.33 |    241.33    |  266.57  |    0.0     |  493.77  |  2.85  |   880.42  |   0.0   |    9.42   | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-12-21 |    840.0    |    930.32    |    0.0     |  0.0  |  0.0   |    50.22     |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-12-20 |    800.05   |    367.2     |    0.0     |  0.0  |  0.0   |    70.57     |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-12-19 |    455.02   |    146.32    |    4.37    |  0.0  | 23.43  |    172.0     |   0.0    |    0.0     |  164.22  |  0.0   |   171.12  |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-12-18 |    676.9    |    807.7     |    0.0     |  0.0  | 109.32 |    429.92    |  523.22  |    0.0     |  366.7   |  0.0   |   904.33  |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-12-17 |    638.45   |   1051.22    |    0.0     |  0.0  | 219.3  |    175.62    |  821.12  |    0.0     |  608.6   | 10.75  |   893.52  |  103.48 |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-12-16 |    199.6    |    879.77    |   518.73   |  0.0  | 39.72  |    307.48    |  900.3   |    0.0     |  869.27  | 479.7  |   799.43  |  143.35 |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-12-15 |    256.15   |    977.68    |   149.85   |  0.0  | 294.0  |    154.82    |  141.83  |    0.0     |  825.05  | 697.37 |   777.97  |  545.38 |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-12-14 |    712.72   |    726.13    |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |  282.22  | 358.72 |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-12-13 |     0.0     |   1002.25    |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-12-12 |    117.37   |    837.68    |    0.0     |  0.0  | 57.55  |    131.0     |   0.0    |    0.0     |  601.07  | 380.93 |   463.52  |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-12-11 |    491.85   |    506.1     |    0.0     |  0.0  | 248.45 |    60.55     |  439.5   |    0.0     |  771.8   | 469.27 |   810.52  |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-12-10 |    335.52   |    814.67    |    0.0     |  0.0  | 122.28 |     0.0      |   0.0    |    0.0     |  515.67  |  0.0   |   921.22  |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-12-09 |    361.43   |    744.03    |    0.0     |  0.0  | 79.12  |     0.0      |  681.83  |    0.0     |  112.4   |  0.0   |   803.75  |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-12-08 |    486.63   |   1113.85    |    0.0     |  0.0  | 38.63  |     0.23     |  37.32   |    0.0     |  28.15   |  0.0   |   829.73  |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-12-07 |    839.8    |   1194.62    |    0.0     |  0.0  |  0.0   |     0.0      |  472.1   |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-12-06 |    68.97    |   1337.27    |    0.0     |  0.0  |  0.0   |     0.0      |  201.5   |    0.0     |   0.0    |  0.0   |    0.0    |  442.03 |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-12-05 |    201.93   |    934.23    |    0.0     |  0.0  | 37.47  |     0.0      |   0.0    |    0.0     |  686.9   |  0.0   |   841.4   |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |

## Custom Configurations
1. Secrets Configuration
  - `SSH_PRIVATE_KEY`: Private SSH key for authenticating with the target server.
  - `SSH_USERNAME`: Username for SSH authentication on the target server.
  - `SERVER_HOST`: Hostname or IP address of the target server.
  - `SSH_PORT` (Optional): Port number for SSH connection (default: 22).
  - `GIT_PUSH_USER_NAME`: Username for GitHub account used for pushing changes to the repository.
  - `GIT_PUSH_USER_EMAIL`: Email address for GitHub account used for pushing changes to the repository.
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
