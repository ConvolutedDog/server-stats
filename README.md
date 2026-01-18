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
|  Total  |     229d    |     266d     |    60d     |  31d  |  84d  |     157d     |   76d    |    13d     |   189d   |  80d  |    157d   |   122d  |    77d    | 12d |     13d     |     4d     |  11d   |    26d     |
| 2026-01 |      10     |      16      |     7      |   0   |   13  |      14      |    14    |     0      |    10    |   15  |     10    |    8    |     3     |  0  |      0      |     0      |   0    |     2      |
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
|    date    | pengbenkang | yangjianchao | pengyinlun | juxin | hello  | shenjunzhong | fengjing | wangjianan | chendong |  hejun  | yangrenyu | xuezeyu | kangyuhan | lzd | yangjingkui | tangminjin | guohui | mashaocong |
|:----------:|:-----------:|:------------:|:----------:|:-----:|:------:|:------------:|:--------:|:----------:|:--------:|:-------:|:---------:|:-------:|:---------:|:---:|:-----------:|:----------:|:------:|:----------:|
|   Total    |    110.0h   |    250.9h    |   29.4h    |  0.0h | 81.2h  |    66.3h     |  222.0h  |    0.0h    |  131.3h  |  152.6h |   205.9h  |  26.4h  |    7.9h   | 0.0h |     0.0h    |    0.0h    |  0.0h  |   31.5h    |
| 2026-01-18 |     0.0     |     0.8      |    0.0     |  0.0  | 314.77 |    101.18    |  61.92   |    0.0     |   0.0    |  104.17 |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2026-01-17 |     0.0     |     0.55     |    0.0     |  0.0  | 334.25 |    89.73     |  818.92  |    0.0     |  23.05   |  29.15  |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2026-01-16 |     0.0     |     0.62     |   130.35   |  0.0  | 348.0  |    117.67    |  832.63  |    0.0     |  745.48  |  661.43 |   623.63  |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2026-01-15 |     0.0     |     0.63     |    0.0     |  0.0  | 394.22 |    487.63    |  762.27  |    0.0     |  702.9   |  718.18 |   899.78  |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2026-01-14 |    62.33    |     0.48     |    0.0     |  0.0  | 333.62 |    399.35    |  756.82  |    0.0     |  266.4   |  687.92 |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2026-01-13 |    187.5    |     0.93     |   134.62   |  0.0  | 138.7  |    252.3     |  836.05  |    0.0     |   0.0    |  252.65 |   822.68  |  230.93 |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2026-01-12 |    23.52    |    507.0     |   138.58   |  0.0  | 353.13 |    51.23     |  811.72  |    0.0     |   0.0    |  523.43 |   760.48  |  405.42 |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2026-01-11 |     0.0     |    551.73    |    0.0     |  0.0  |  0.0   |     0.0      |  630.9   |    0.0     |   0.0    |  33.23  |    0.0    |   6.02  |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2026-01-10 |    519.82   |   1055.63    |    0.0     |  0.0  |  0.0   |    102.12    |  169.7   |    0.0     |  18.43   |  123.4  |    0.0    |  148.2  |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |   817.72   |
| 2026-01-09 |    254.38   |    553.12    |    0.0     |  0.0  | 202.08 |    51.42     |  454.48  |    0.0     |  370.98  | 1102.95 |   456.67  |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |   709.8    |
| 2026-01-08 |     0.3     |    877.38    |   39.55    |  0.0  | 325.57 |    10.47     |  877.8   |    0.0     |  26.18   |  651.25 |   850.08  |  39.78  |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2026-01-07 |    310.6    |    892.32    |    0.0     |  0.0  | 203.38 |    215.78    |  930.63  |    0.0     |  516.43  |  953.58 |   899.0   |  362.65 |   58.05   | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2026-01-06 |    324.25   |    554.75    |   140.57   |  0.0  |  38.9  |    289.62    |  738.32  |    0.0     |   0.0    |  675.33 |   785.38  |  188.5  |   307.85  | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2026-01-05 |    339.05   |    442.22    |   124.02   |  0.0  | 249.3  |    447.97    |  844.17  |    0.0     |  188.15  |  649.57 |   790.53  |  202.93 |   93.57   | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2026-01-04 |     0.0     |    458.33    |   108.3    |  0.0  | 255.65 |    107.08    |   0.0    |    0.0     |  144.3   |  194.27 |   393.67  |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2026-01-03 |     0.0     |     0.0      |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |   0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2026-01-02 |     0.0     |     0.0      |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |   0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2026-01-01 |    135.5    |     0.82     |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |   0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-12-31 |     0.0     |     0.0      |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |   0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-12-30 |    158.45   |    693.6     |   307.22   |  0.0  | 230.2  |    218.43    |  909.82  |    0.0     | 1379.92  |  71.65  |   452.7   |   0.0   |    6.35   | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-12-29 |    194.37   |    791.12    |   177.28   |  0.0  | 165.45 |    119.35    |  787.65  |    0.0     |  459.02  |  685.7  |   766.3   |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |   361.2    |
| 2025-12-28 |     0.0     |     0.0      |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |   0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-12-27 |    400.3    |    854.68    |    0.0     |  0.0  |  0.0   |    103.08    |  837.37  |    0.0     |  659.52  |   0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-12-26 |     0.0     |   1130.73    |    0.0     |  0.0  |  0.0   |     0.0      |  492.08  |    0.0     |  319.3   |  734.62 |   420.18  |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-12-25 |    506.13   |   1360.97    |    0.0     |  0.0  | 326.22 |    56.22     |  132.58  |    0.0     |  25.05   |  302.68 |   903.42  |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-12-24 |    657.08   |    889.5     |    0.0     |  0.0  | 363.22 |    49.08     |  366.33  |    0.0     |  813.47  |   0.0   |   831.62  |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-12-23 |    441.63   |   1329.95    |   376.83   |  0.0  | 105.13 |    346.43    |   0.0    |    0.0     |  724.77  |   0.0   |   815.45  |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-12-22 |    443.67   |    810.05    |    86.6    |  0.0  | 190.33 |    241.33    |  266.57  |    0.0     |  493.77  |   2.85  |   880.42  |   0.0   |    9.42   | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-12-21 |    840.0    |    930.32    |    0.0     |  0.0  |  0.0   |    50.22     |   0.0    |    0.0     |   0.0    |   0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-12-20 |    800.05   |    367.2     |    0.0     |  0.0  |  0.0   |    70.57     |   0.0    |    0.0     |   0.0    |   0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |

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
