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
|  Total  |     261d    |     305d     |    63d     |  33d  |  106d |     180d     |   89d    |    24d     |   224d   |  93d  |    172d   |   141d  |    90d    | 12d |     13d     |     4d     |  11d   |    43d     |
| 2026-02 |      24     |      26      |     0      |   1   |   9   |      10      |    4     |     11     |    24    |   9   |     5     |    7    |     4     |  0  |      0      |     0      |   0    |     13     |
| 2026-01 |      18     |      29      |     10     |   1   |   26  |      27      |    23    |     0      |    21    |   19  |     20    |    20   |     12    |  0  |      0      |     0      |   0    |     6      |
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
|    date    | pengbenkang | yangjianchao | pengyinlun | juxin  | hello  | shenjunzhong | fengjing | wangjianan | chendong |  hejun  | yangrenyu | xuezeyu | kangyuhan | lzd | yangjingkui | tangminjin | guohui | mashaocong |
|:----------:|:-----------:|:------------:|:----------:|:------:|:------:|:------------:|:--------:|:----------:|:--------:|:-------:|:---------:|:-------:|:---------:|:---:|:-----------:|:----------:|:------:|:----------:|
|   Total    |    216.9h   |    61.0h     |    0.0h    |  3.7h  | 72.5h  |    85.3h     |  54.5h   |   36.4h    |  236.3h  |  41.4h  |   45.8h   |  40.0h  |    9.6h   | 0.0h |     0.0h    |    0.0h    |  0.0h  |   151.7h   |
| 2026-02-28 |    690.27   |     29.1     |    0.0     |  0.0   | 607.97 |    875.08    |   0.0    |    0.0     |  471.03  |  179.65 |    0.0    |   0.0   |   228.98  | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2026-02-27 |    335.1    |     0.98     |    0.0     |  0.0   |  0.0   |     0.0      |   0.0    |    0.0     |  525.37  |   0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2026-02-26 |    817.38   |     0.9      |    0.0     |  0.0   | 703.7  |     0.0      |   0.0    |    0.0     |  626.75  |   0.65  |    0.0    |  72.85  |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |   795.7    |
| 2026-02-25 |    678.8    |    85.32     |    0.0     |  0.0   | 1295.5 |     0.0      |   0.0    |    5.1     |  680.75  |  136.02 |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |   456.7    |
| 2026-02-24 |    873.27   |    524.93    |    0.0     |  0.0   | 16.03  |     0.0      |   0.0    |    3.8     |  835.8   |   0.0   |    0.0    |  186.17 |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |   809.9    |
| 2026-02-23 |    689.25   |     1.08     |    0.0     |  0.0   | 39.85  |     0.0      |   0.0    |    0.0     |   0.0    |   0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |   660.48   |
| 2026-02-22 |   1205.77   |     0.93     |    0.0     |  0.0   |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |   0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |  1369.13   |
| 2026-02-21 |    226.53   |     0.87     |    0.0     |  0.0   |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |   0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |   799.65   |
| 2026-02-20 |    903.68   |     1.27     |    0.0     |  0.0   |  0.0   |     0.0      |   0.0    |    0.0     |  275.9   |   0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |   656.28   |
| 2026-02-19 |     0.0     |     0.83     |    0.0     |  0.0   |  0.0   |    793.72    |   0.0    |    0.0     |  242.95  |   0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |   399.57   |
| 2026-02-18 |    805.98   |     0.67     |    0.0     |  0.0   |  0.0   |     0.0      |   0.0    |    0.0     | 1272.98  |   0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |   26.92    |
| 2026-02-17 |     0.0     |     0.67     |    0.0     |  0.0   |  0.0   |     0.0      |   0.0    |    0.0     |  225.03  |   0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |   639.0    |
| 2026-02-16 |     5.02    |     0.8      |    0.0     |  0.0   |  0.0   |    544.22    |   0.0    |    0.0     |  736.42  |   0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2026-02-15 |    304.92   |     0.5      |    0.0     |  0.0   |  0.0   |     0.0      |   0.0    |    0.0     |  60.47   |   0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2026-02-14 |   1222.08   |     0.78     |    0.0     |  0.0   |  0.0   |    850.27    |   0.0    |   443.9    |  426.67  |   0.0   |    0.0    |  245.93 |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2026-02-13 |    808.5    |     0.82     |    0.0     |  0.0   |  0.0   |    83.83     |   0.0    |   411.02   |  567.65  |   0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2026-02-12 |    540.4    |     0.0      |    0.0     |  0.0   |  0.0   |    219.7     |   0.0    |   325.12   |  410.9   |   0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2026-02-11 |    338.77   |     0.53     |    0.0     |  0.0   |  0.0   |    22.35     |   0.0    |    50.0    |  625.45  |  444.2  |    0.0    |  293.82 |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2026-02-10 |    395.8    |     0.0      |    0.0     |  0.0   |  0.0   |     0.0      |   0.0    |   288.0    |  315.35  | 1398.75 |   273.13  |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2026-02-09 |    88.47    |     69.8     |    0.0     |  0.0   |  0.0   |     0.0      |   0.0    |    0.0     |  519.43  |  309.62 |    0.0    |   0.0   |    43.2   | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2026-02-08 |    33.02    |     0.88     |    0.0     |  0.0   |  0.0   |     0.0      |   0.0    |    0.0     |  33.65   |  14.52  |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2026-02-07 |     0.0     |     0.52     |    0.0     |  0.0   |  0.0   |     0.0      |   0.0    |    0.0     |  389.57  |   0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2026-02-06 |    321.5    |    67.38     |    0.0     |  0.0   |  0.0   |     0.0      |  869.4   |   20.53    |  677.13  |   0.0   |   484.08  |   0.0   |    83.6   | 0.0 |     0.0     |    0.0     |  0.0   |   689.83   |
| 2026-02-05 |    484.28   |    266.05    |    0.0     |  0.0   |  0.0   |     0.0      |  708.5   |   296.57   | 1371.85  |   0.0   |   452.97  |   0.0   |   83.67   | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2026-02-04 |    490.37   |    484.02    |    0.0     |  0.0   | 122.12 |     0.0      |  361.47  |   120.55   |  822.88  |   0.6   |   810.62  |  227.55 |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2026-02-03 |    392.33   |    181.4     |    0.0     | 221.07 | 517.98 |    298.3     |  442.52  |   216.8    |  526.68  |   0.0   |    0.0    |  474.15 |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |   911.23   |
| 2026-02-02 |    358.6    |    729.07    |    0.0     |  0.0   | 422.55 |    576.58    |   0.0    |    0.0     |  716.75  |   0.0   |   302.18  |  526.58 |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |   885.08   |
| 2026-02-01 |     0.0     |    141.12    |    0.0     |  0.0   | 322.88 |    110.62    |   0.0    |    0.0     |   0.0    |   0.03  |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2026-01-31 |     1.25    |    141.88    |    0.0     |  0.0   | 119.18 |    364.63    |   0.0    |    0.0     |  280.0   |   0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2026-01-30 |     0.0     |    928.9     |    0.0     |  0.0   | 183.37 |    377.4     |  885.28  |    0.0     |  540.0   |   0.0   |   425.03  |  372.38 |   139.25  | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |

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
