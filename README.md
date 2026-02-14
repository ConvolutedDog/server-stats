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
|  Total  |     249d    |     291d     |    63d     |  33d  |  101d |     177d     |   89d    |    22d     |   213d   |  90d  |    172d   |   139d  |    89d    | 12d |     13d     |     4d     |  11d   |    33d     |
| 2026-02 |      12     |      12      |     0      |   1   |   4   |      7       |    4     |     9      |    13    |   6   |     5     |    5    |     3     |  0  |      0      |     0      |   0    |     3      |
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
|   Total    |    112.9h   |    183.6h    |    6.5h    |  4.2h  | 100.0h |    87.4h     |  166.9h  |   36.2h    |  291.3h  |  74.9h  |   173.6h  |  132.5h |   41.3h   | 0.0h |     0.0h    |    0.0h    |  0.0h  |   83.1h    |
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
| 2026-01-29 |    297.88   |    694.08    |    0.0     | 31.87  | 294.2  |    130.53    |  763.2   |    0.0     |  538.95  |  399.3  |   582.77  |  503.95 |   158.68  | 0.0 |     0.0     |    0.0     |  0.0   |   1127.4   |
| 2026-01-28 |     0.0     |   1077.53    |    0.0     |  0.0   | 269.67 |    324.45    |  565.18  |    0.0     | 1283.37  |   0.0   |   752.73  |  962.18 |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |   379.98   |
| 2026-01-27 |    93.65    |    737.68    |    0.0     |  0.0   | 127.5  |    220.15    |  655.67  |    0.0     | 1310.37  |   0.0   |   784.02  |  560.0  |   225.5   | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2026-01-26 |    363.65   |    808.57    |    0.0     |  0.0   | 338.62 |    344.87    |   0.0    |    0.0     |  767.73  |   0.0   |   879.5   |  693.35 |    8.15   | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2026-01-25 |    173.12   |    885.65    |    0.0     |  0.0   | 309.83 |    219.38    |   0.0    |    0.0     |   0.0    |   0.0   |    0.0    |  237.4  |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2026-01-24 |     0.0     |    920.13    |    0.0     |  0.0   | 192.37 |    207.97    |  173.52  |    0.0     |   0.0    |   0.0   |    0.0    |  65.37  |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2026-01-23 |     0.28    |    450.85    |   94.53    |  0.0   | 275.22 |    33.53     |   0.0    |    0.0     |  930.0   |   0.05  |   694.1   |  291.72 |   417.6   | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2026-01-22 |    226.32   |    727.72    |    0.0     |  0.0   | 299.35 |     2.82     |  488.02  |    0.0     | 1390.82  |  555.03 |   768.67  |  815.07 |   406.3   | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2026-01-21 |     0.0     |    540.55    |   89.48    |  0.0   | 337.52 |     7.2      |  765.38  |    0.0     |  912.4   |   0.0   |   858.1   |  466.77 |   456.63  | 0.0 |     0.0     |    0.0     |  0.0   |   135.3    |
| 2026-01-20 |    141.55   |    437.37    |   72.87    |  0.0   | 402.32 |    222.28    |  910.25  |    0.0     |  832.23  |   0.0   |   881.42  |  871.6  |   178.17  | 0.0 |     0.0     |    0.0     |  0.0   |   855.62   |
| 2026-01-19 |     0.0     |    722.25    |    0.0     |  0.0   | 468.62 |    318.53    |  712.4   |    0.0     |  518.65  |  578.93 |   845.85  |  345.05 |   278.73  | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2026-01-18 |     0.0     |     0.8      |    0.0     |  0.0   | 314.77 |    101.18    |  61.92   |    0.0     |   0.0    |  104.17 |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2026-01-17 |     0.0     |     0.55     |    0.0     |  0.0   | 334.25 |    89.73     |  818.92  |    0.0     |  23.05   |  29.15  |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2026-01-16 |     0.0     |     0.62     |   130.35   |  0.0   | 348.0  |    117.67    |  832.63  |    0.0     |  745.48  |  661.43 |   623.63  |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |

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
