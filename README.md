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
|  Total  |     138d    |     160d     |    32d     |  30d  |  31d  |     94d      |   36d    |    13d     |   115d   |  26d  |    89d    |   82d   |    65d    | 12d |     13d     |     2d     |  11d   |    10d     |
| 2025-09 |      28     |      29      |     0      |   0   |   3   |      12      |    13    |     2      |    23    |   14  |     21    |    6    |     12    |  0  |      1      |     0      |   0    |     3      |
| 2025-08 |      12     |      29      |     1      |   0   |   0   |      23      |    0     |     5      |    25    |   0   |     6     |    14   |     15    |  0  |      1      |     0      |   0    |     2      |
| 2025-07 |      29     |      29      |     4      |   0   |   4   |      19      |    10    |     0      |    23    |   3   |     19    |    23   |     12    |  2  |      0      |     1      |   11   |     5      |
| 2025-06 |      28     |      28      |     3      |   8   |   6   |      20      |    10    |     0      |    26    |   6   |     11    |    18   |     15    |  7  |      5      |     0      |   0    |     0      |
| 2025-05 |      23     |      26      |     15     |   8   |   9   |      9       |    0     |     3      |    13    |   1   |     19    |    11   |     7     |  2  |      6      |     1      |   0    |     0      |
| 2025-04 |      18     |      19      |     9      |   14  |   9   |      11      |    3     |     3      |    5     |   2   |     13    |    10   |     4     |  1  |      0      |     0      |   0    |     0      |

## Daily login time in minutes for the past 30 days
|    date    | pengbenkang | yangjianchao | pengyinlun | juxin | hello  | shenjunzhong | fengjing | wangjianan | chendong | hejun  | yangrenyu | xuezeyu | kangyuhan | lzd | yangjingkui | tangminjin | guohui | mashaocong |
|:----------:|:-----------:|:------------:|:----------:|:-----:|:------:|:------------:|:--------:|:----------:|:--------:|:------:|:---------:|:-------:|:---------:|:---:|:-----------:|:----------:|:------:|:----------:|
|   Total    |    217.1h   |    399.2h    |    0.0h    |  0.0h |  9.3h  |    33.4h     |  123.2h  |    9.8h    |  210.0h  | 67.4h  |   196.5h  |  51.3h  |   73.7h   | 0.0h |     0.1h    |    0.0h    |  0.0h  |    7.3h    |
| 2025-09-30 |    682.13   |    898.2     |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |  228.37  | 365.38 |   735.47  |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-09-29 |    573.93   |   1324.77    |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |  616.97  | 103.25 |   808.05  |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-09-28 |    574.47   |    896.5     |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |  662.55  | 90.27  |   681.2   |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-09-27 |    470.42   |    937.75    |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    | 542.17 |    0.0    |  614.72 |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-09-26 |    475.88   |    877.82    |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |  576.12  |  1.58  |   590.5   |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-09-25 |    455.03   |     0.37     |    0.0     |  0.0  | 217.08 |     0.0      |   0.0    |    0.0     |  804.42  | 28.67  |   787.82  |  182.1  |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-09-24 |    668.38   |    941.13    |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |  512.58  | 296.13 |   604.08  |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-09-23 |    573.62   |    910.48    |    0.0     |  0.0  |  0.0   |    79.67     |   0.0    |    0.0     |   0.0    | 696.15 |   363.8   |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-09-22 |    483.82   |    854.57    |    0.0     |  0.0  |  0.0   |    215.5     |   0.0    |    0.0     |   0.97   | 513.02 |   326.72  |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    1.3     |
| 2025-09-21 |    396.05   |    966.88    |    0.0     |  0.0  |  0.0   |     80.9     |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-09-20 |    361.8    |    965.07    |    0.0     |  0.0  |  0.0   |    124.95    |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-09-19 |    475.02   |    882.45    |    0.0     |  0.0  |  0.0   |     0.0      |  852.97  |    0.0     |  583.33  | 20.23  |   367.97  |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-09-18 |    470.48   |   1093.42    |    0.0     |  0.0  |  0.0   |    59.47     |  352.02  |    0.0     |  847.25  | 529.75 |   214.53  |   0.0   |    0.0    | 0.0 |     4.08    |    0.0     |  0.0   |    0.72    |
| 2025-09-17 |    526.73   |   1123.62    |    0.0     |  0.0  |  0.0   |    520.67    |  827.05  |    0.0     |  774.93  | 415.55 |   740.82  |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-09-16 |    572.92   |    696.47    |    0.0     |  0.0  | 112.47 |    421.32    |  474.23  |    0.0     | 1175.25  | 368.17 |   600.52  |  511.97 |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-09-15 |    436.28   |   1271.35    |    0.0     |  0.0  |  0.0   |    127.08    |   0.0    |    0.0     |  738.87  | 75.53  |   348.82  |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-09-14 |    406.15   |    1217.9    |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |  553.48 |   555.43  | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-09-13 |    242.85   |   1098.47    |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |  606.63 |   494.05  | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-09-12 |    277.88   |    899.35    |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |  504.53  |  0.0   |   473.8   |  608.92 |   460.95  | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-09-11 |    295.02   |    871.12    |    0.0     |  0.0  |  0.0   |     0.0      |  908.07  |    0.0     |  681.52  |  0.0   |   744.78  |   0.0   |   543.35  | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-09-10 |    767.07   |    782.5     |    0.0     |  0.0  |  0.0   |     0.0      |  545.17  |    0.0     |  615.52  |  0.0   |   781.9   |   0.0   |   486.62  | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-09-09 |    914.4    |    897.18    |    0.0     |  0.0  |  0.0   |     0.0      |  110.62  |    0.0     |  807.45  |  0.0   |   821.9   |   0.0   |   358.33  | 0.0 |     0.0     |    0.0     |  0.0   |   437.83   |
| 2025-09-08 |    693.15   |    820.75    |    0.0     |  0.0  |  0.0   |     0.0      |  704.8   |    0.0     |  420.53  |  0.0   |   632.9   |   0.0   |   464.58  | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-09-07 |    213.33   |    804.27    |    0.0     |  0.0  |  0.0   |    234.17    |  729.53  |    0.0     |  57.02   |  0.0   |    0.0    |   0.0   |   482.62  | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-09-06 |    105.62   |    577.97    |    0.0     |  0.0  |  0.0   |    112.77    |  722.6   |    0.0     |  772.8   |  0.0   |    0.0    |   0.0   |    45.0   | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-09-05 |     0.0     |    122.18    |    0.0     |  0.0  |  0.0   |     0.0      |  134.32  |    0.0     |   0.05   |  0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-09-04 |    206.12   |    284.38    |    0.0     |  0.0  |  0.0   |     0.0      |  527.42  |    0.0     |  149.53  |  0.0   |   342.33  |   0.0   |   152.37  | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-09-03 |    348.1    |    530.98    |    0.0     |  0.0  | 228.85 |     16.8     |  503.58  |   350.83   |  474.63  |  0.0   |   476.3   |   0.0   |   229.27  | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-09-02 |    361.8    |    402.78    |    0.0     |  0.0  |  0.0   |    11.98     |   0.0    |   235.62   |  597.4   |  0.0   |   348.13  |   0.0   |   146.88  | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-09-01 |     0.0     |     0.0      |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |

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
