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
|  Total  |     111d    |     131d     |    32d     |  30d  |  29d  |     83d      |   25d    |    13d     |   92d    |  12d  |    69d    |   75d   |    54d    | 12d |     12d     |     2d     |  11d   |     7d     |
| 2025-09 |      2      |      3       |     0      |   0   |   1   |      2       |    2     |     2      |    3     |   0   |     2     |    0    |     2     |  0  |      0      |     0      |   0    |     0      |
| 2025-08 |      11     |      26      |     1      |   0   |   0   |      22      |    0     |     5      |    22    |   0   |     5     |    13   |     14    |  0  |      1      |     0      |   0    |     2      |
| 2025-07 |      29     |      29      |     4      |   0   |   4   |      19      |    10    |     0      |    23    |   3   |     19    |    23   |     12    |  2  |      0      |     1      |   11   |     5      |
| 2025-06 |      28     |      28      |     3      |   8   |   6   |      20      |    10    |     0      |    26    |   6   |     11    |    18   |     15    |  7  |      5      |     0      |   0    |     0      |
| 2025-05 |      23     |      26      |     15     |   8   |   9   |      9       |    0     |     3      |    13    |   1   |     19    |    11   |     7     |  2  |      6      |     1      |   0    |     0      |
| 2025-04 |      18     |      19      |     9      |   14  |   9   |      11      |    3     |     3      |    5     |   2   |     13    |    10   |     4     |  1  |      0      |     0      |   0    |     0      |

## Daily login time in minutes for the past 30 days
|    date    | pengbenkang | yangjianchao | pengyinlun | juxin | hello  | shenjunzhong | fengjing | wangjianan | chendong | hejun | yangrenyu | xuezeyu | kangyuhan | lzd | yangjingkui | tangminjin | guohui | mashaocong |
|:----------:|:-----------:|:------------:|:----------:|:-----:|:------:|:------------:|:--------:|:----------:|:--------:|:-----:|:---------:|:-------:|:---------:|:---:|:-----------:|:----------:|:------:|:----------:|
|   Total    |    75.2h    |    60.6h     |    0.0h    |  0.0h |  3.8h  |    127.6h    |  10.6h   |   32.0h    |  271.8h  |  0.0h |   63.0h   |  49.8h  |   37.5h   | 0.0h |     0.1h    |    0.0h    |  0.0h  |    0.5h    |
| 2025-09-05 |     0.0     |    122.18    |    0.0     |  0.0  |  0.0   |     0.0      |  134.32  |    0.0     |   0.05   |  0.0  |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-09-03 |    348.1    |    530.98    |    0.0     |  0.0  | 228.85 |     16.8     |  503.58  |   350.83   |  474.63  |  0.0  |   476.3   |   0.0   |   229.27  | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-09-02 |    361.8    |    402.78    |    0.0     |  0.0  |  0.0   |    11.98     |   0.0    |   235.62   |  597.4   |  0.0  |   348.13  |   0.0   |   146.88  | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-08-28 |    402.12   |    466.42    |    0.0     |  0.0  |  0.0   |    367.53    |   0.0    |    0.0     |  850.4   |  0.0  |   616.35  |  413.85 |   214.75  | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-08-27 |    169.02   |     0.83     |    0.0     |  0.0  |  0.0   |    535.35    |   0.0    |    0.0     |   22.0   |  0.0  |   831.2   |  387.77 |   179.82  | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-08-26 |    141.05   |    887.9     |    1.58    |  0.0  |  0.0   |    564.37    |   0.0    |    0.0     |  167.42  |  0.0  |   842.75  |  388.17 |   122.15  | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-08-25 |    182.38   |    733.63    |    0.0     |  0.0  |  0.0   |    522.23    |   0.0    |    0.0     |  815.93  |  0.0  |   520.28  |  221.4  |   45.93   | 0.0 |     8.5     |    0.0     |  0.0   |    0.0     |
| 2025-08-24 |    466.27   |     0.77     |    0.0     |  0.0  |  0.0   |    375.98    |   0.0    |    0.9     |   0.0    |  0.0  |    0.0    |   0.0   |   104.57  | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-08-23 |     0.0     |     0.75     |    0.0     |  0.0  |  0.0   |    210.78    |   0.0    |    0.0     |   0.0    |  0.0  |    0.0    |   0.0   |   37.63   | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-08-22 |    536.52   |     0.85     |    0.0     |  0.0  |  0.0   |    147.68    |   0.0    |   121.45   |  510.37  |  0.0  |    0.0    |   0.27  |   108.62  | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-08-21 |    804.53   |     0.8      |    0.0     |  0.0  |  0.0   |    532.27    |   0.0    |   292.4    |  451.67  |  0.0  |    0.0    |  485.75 |   15.58   | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-08-20 |     0.0     |    29.33     |    0.0     |  0.0  |  0.0   |    237.17    |   0.0    |   520.53   |  664.68  |  0.0  |    0.0    |  116.68 |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-08-19 |     0.0     |    424.95    |    0.0     |  0.0  |  0.0   |    527.25    |   0.0    |   399.87   |  752.77  |  0.0  |    0.0    |  54.28  |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-08-18 |     0.0     |     0.83     |    0.0     |  0.0  |  0.0   |    565.2     |   0.0    |    0.0     |  590.1   |  0.0  |    0.0    |  200.28 |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |   28.57    |
| 2025-08-17 |     0.0     |     0.78     |    0.0     |  0.0  |  0.0   |    537.03    |   0.0    |    0.0     |   0.0    |  0.0  |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-08-16 |     0.0     |     0.83     |    0.0     |  0.0  |  0.0   |    262.28    |   0.0    |    0.0     |  410.45  |  0.0  |    0.0    |  59.08  |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-08-15 |     0.0     |     0.73     |    0.0     |  0.0  |  0.0   |    506.95    |   0.0    |    0.0     |  798.68  |  0.0  |    0.0    |  289.28 |   193.93  | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-08-14 |     0.0     |     0.88     |    0.0     |  0.0  |  0.0   |    393.93    |   0.0    |    0.0     |  722.28  |  0.0  |    0.0    |  305.13 |   233.98  | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-08-13 |     0.0     |     0.47     |    0.0     |  0.0  |  0.0   |    111.37    |   0.0    |    0.0     |  520.38  |  0.0  |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-08-11 |     0.0     |     0.73     |    0.0     |  0.0  |  0.0   |    31.67     |   0.0    |    0.0     |  738.77  |  0.0  |    0.0    |  20.05  |   240.42  | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-08-10 |     0.0     |     0.62     |    0.0     |  0.0  |  0.0   |    74.18     |   0.0    |    0.0     |  479.85  |  0.0  |    0.0    |   0.0   |   163.92  | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-08-09 |     0.0     |     0.52     |    0.0     |  0.0  |  0.0   |    191.2     |   0.0    |    0.0     |  422.2   |  0.0  |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-08-07 |     0.0     |     0.6      |    0.0     |  0.0  |  0.0   |    371.93    |   0.0    |    0.0     |  1010.0  |  0.0  |    0.0    |   0.0   |    76.6   | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-08-06 |     0.0     |     0.57     |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |  877.53  |  0.0  |    0.0    |   0.0   |   134.6   | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-08-05 |     0.0     |     0.63     |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |  881.53  |  0.0  |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-08-04 |    40.77    |     0.52     |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     | 1222.87  |  0.0  |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-08-03 |    315.02   |     0.62     |    0.0     |  0.0  |  0.0   |    38.68     |   0.0    |    0.0     |  638.68  |  0.0  |    0.07   |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-08-02 |    203.05   |     0.58     |    0.0     |  0.0  |  0.0   |    98.03     |   0.0    |    0.0     |   0.0    |  0.0  |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-08-01 |    403.28   |     4.65     |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |  641.57  |  0.0  |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.6     |
| 2025-07-31 |    139.05   |    16.78     |    0.0     |  0.0  |  0.0   |    425.23    |   0.0    |    0.0     | 1047.62  |  0.0  |   142.22  |  43.67  |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |

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
