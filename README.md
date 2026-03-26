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
|  month  | pengbenkang | yangjianchao | pengyinlun | juxin | hello | shenjunzhong | fengjing | wangjianan | chendong | hejun | yangrenyu | xuezeyu | kangyuhan | lzd | yangjingkui | tangminjin | guohui | mashaocong | shiyang |
|:-------:|:-----------:|:------------:|:----------:|:-----:|:-----:|:------------:|:--------:|:----------:|:--------:|:-----:|:---------:|:-------:|:---------:|:---:|:-----------:|:----------:|:------:|:----------:|:-------:|
|  Total  |     279d    |     331d     |    76d     |  39d  |  130d |     202d     |   98d    |    35d     |   238d   |  102d |    184d   |   162d  |    97d    | 14d |     13d     |     4d     |  11d   |    45d     |    1d   |
| 2026-03 |      18     |      26      |     13     |   6   |   24  |      22      |    9     |     11     |    14    |   9   |     12    |    21   |     7     |  2  |      0      |     0      |   0    |     2      |    1    |
| 2026-02 |      24     |      26      |     0      |   1   |   9   |      10      |    4     |     11     |    24    |   9   |     5     |    7    |     4     |  0  |      0      |     0      |   0    |     13     |    0    |
| 2026-01 |      18     |      29      |     10     |   1   |   26  |      27      |    23    |     0      |    21    |   19  |     20    |    20   |     12    |  0  |      0      |     0      |   0    |     6      |    0    |
| 2025-12 |      27     |      29      |     8      |   0   |   21  |      18      |    19    |     0      |    24    |   14  |     22    |    5    |     2     |  0  |      0      |     0      |   0    |     3      |    0    |
| 2025-11 |      29     |      30      |     8      |   1   |   14  |      15      |    6     |     0      |    19    |   13  |     18    |    13   |     5     |  0  |      0      |     2      |   0    |     11     |    0    |
| 2025-10 |      25     |      31      |     5      |   0   |   5   |      16      |    1     |     0      |    21    |   12  |     18    |    14   |     2     |  0  |      0      |     0      |   0    |     0      |    0    |
| 2025-09 |      28     |      29      |     0      |   0   |   3   |      12      |    13    |     2      |    23    |   14  |     21    |    6    |     12    |  0  |      1      |     0      |   0    |     3      |    0    |
| 2025-08 |      12     |      29      |     1      |   0   |   0   |      23      |    0     |     5      |    25    |   0   |     6     |    14   |     15    |  0  |      1      |     0      |   0    |     2      |    0    |
| 2025-07 |      29     |      29      |     4      |   0   |   4   |      19      |    10    |     0      |    23    |   3   |     19    |    23   |     12    |  2  |      0      |     1      |   11   |     5      |    0    |
| 2025-06 |      28     |      28      |     3      |   8   |   6   |      20      |    10    |     0      |    26    |   6   |     11    |    18   |     15    |  7  |      5      |     0      |   0    |     0      |    0    |
| 2025-05 |      23     |      26      |     15     |   8   |   9   |      9       |    0     |     3      |    13    |   1   |     19    |    11   |     7     |  2  |      6      |     1      |   0    |     0      |    0    |
| 2025-04 |      18     |      19      |     9      |   14  |   9   |      11      |    3     |     3      |    5     |   2   |     13    |    10   |     4     |  1  |      0      |     0      |   0    |     0      |    0    |

## Daily login time in minutes for the past 30 days
|    date    | pengbenkang | yangjianchao | pengyinlun | juxin  | hello  | shenjunzhong | fengjing | wangjianan | chendong | hejun  | yangrenyu | xuezeyu | kangyuhan |  lzd  | yangjingkui | tangminjin | guohui | mashaocong | shiyang |
|:----------:|:-----------:|:------------:|:----------:|:------:|:------:|:------------:|:--------:|:----------:|:--------:|:------:|:---------:|:-------:|:---------:|:-----:|:-----------:|:----------:|:------:|:----------:|:-------:|
|   Total    |    164.6h   |    89.4h     |   119.0h   | 26.3h  | 215.1h |    122.5h    |  105.8h  |   52.2h    |  155.9h  | 48.9h  |   126.1h  |  195.3h |   20.6h   |  0.8h |     0.0h    |    0.0h    |  0.0h  |   46.2h    |   0.6h  |
| 2026-03-26 |    87.53    |     0.83     |    0.0     |  0.0   | 432.97 |     0.0      |  423.18  |   926.05   |  73.47   |  0.0   |   964.25  |  471.92 |    0.0    | 44.72 |     0.0     |    0.0     |  0.0   |    0.0     |  33.87  |
| 2026-03-25 |     0.0     |     0.85     |    0.0     |  0.0   |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    |  0.0  |     0.0     |    0.0     |  0.0   |    0.0     |   0.0   |
| 2026-03-24 |     0.0     |     0.82     |    0.0     |  0.0   |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    | 1270.13 |    0.0    |  0.0  |     0.0     |    0.0     |  0.0   |    0.0     |   0.0   |
| 2026-03-23 |     0.0     |     0.75     |    0.0     |  0.0   | 796.32 |    796.58    |  29.33   |    0.0     |  804.87  |  0.0   |   967.5   |  60.68  |    0.0    |  0.0  |     0.0     |    0.0     |  0.0   |    0.0     |   0.0   |
| 2026-03-22 |     0.0     |     1.22     |   697.85   | 391.0  | 572.83 |    340.22    |  614.82  |    0.0     |   0.0    |  0.0   |    0.0    |  314.13 |   108.28  |  0.0  |     0.0     |    0.0     |  0.0   |    0.0     |   0.0   |
| 2026-03-21 |     0.0     |     1.28     |   449.0    | 545.03 | 364.87 |    372.62    |  874.22  |    0.0     |   0.0    |  0.0   |    0.0    |  707.72 |    0.0    |  0.0  |     0.0     |    0.0     |  0.0   |    0.0     |   0.0   |
| 2026-03-20 |    197.23   |     0.82     |   849.72   | 242.58 | 213.35 |    266.4     | 1331.15  |    0.0     |   0.0    | 86.43  |   480.98  |  824.32 |    0.0    |  0.0  |     0.0     |    0.0     |  0.0   |    0.0     |   0.0   |
| 2026-03-19 |    177.02   |    107.65    |  1127.08   | 138.72 | 542.92 |    390.8     |  830.87  |   262.45   |  53.12   | 558.65 |   627.2   |  425.73 |   539.77  |  0.0  |     0.0     |    0.0     |  0.0   |    0.0     |   0.0   |
| 2026-03-18 |   1011.05   |     0.97     |   338.7    |  0.0   | 298.25 |    550.12    | 1106.57  |   282.92   |   0.0    |  0.0   |   765.38  | 1188.28 |    0.0    |  0.0  |     0.0     |    0.0     |  0.0   |    0.0     |   0.0   |
| 2026-03-17 |    611.62   |    732.88    |   751.6    |  0.0   | 450.18 |    430.58    |  584.77  |   360.4    |  308.4   | 417.45 |   586.18  | 1324.05 |   36.42   |  3.72 |     0.0     |    0.0     |  0.0   |    0.0     |   0.0   |
| 2026-03-16 |   1438.73   |    880.47    |   809.68   |  0.0   | 279.27 |    249.83    |  555.18  |   350.5    |   0.0    | 391.48 |   380.9   |  534.42 |    0.0    |  0.0  |     0.0     |    0.0     |  0.0   |    0.0     |   0.0   |
| 2026-03-15 |    727.3    |    774.62    |   496.92   |  0.0   |  19.4  |    288.17    |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |  413.55 |    0.0    |  0.0  |     0.0     |    0.0     |  0.0   |    0.0     |   0.0   |
| 2026-03-14 |    497.23   |    615.92    |   526.25   |  0.0   | 21.08  |    336.77    |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |  672.98 |    0.0    |  0.0  |     0.0     |    0.0     |  0.0   |    0.0     |   0.0   |
| 2026-03-13 |    281.13   |    534.07    |   479.25   |  0.0   | 273.43 |    336.05    |   0.0    |    0.0     |   0.0    |  0.0   |   379.98  |  541.12 |   20.45   |  0.0  |     0.0     |    0.0     |  0.0   |    0.0     |   0.0   |
| 2026-03-12 |    16.12    |    443.37    |    0.0     |  0.0   | 489.47 |     92.2     |   0.0    |    0.0     |  19.43   | 133.4  |   434.35  |  260.12 |   142.03  |  0.0  |     0.0     |    0.0     |  0.0   |    0.0     |   0.0   |
| 2026-03-11 |    195.22   |    101.38    |   133.6    |  19.9  | 415.58 |    89.97     |   0.0    |   151.5    |   5.48   |  0.0   |   591.62  |  297.1  |    78.1   |  0.0  |     0.0     |    0.0     |  0.0   |    0.0     |   0.0   |
| 2026-03-10 |     0.0     |    274.65    |   287.57   |  0.0   | 674.3  |    125.3     |   0.0    |   359.2    |  714.92  | 515.13 |   864.88  |  463.8  |   83.98   |  0.0  |     0.0     |    0.0     |  0.0   |    0.0     |   0.0   |
| 2026-03-09 |    77.35    |    368.25    |   195.15   |  0.0   | 608.9  |    501.13    |   0.0    |   367.98   |  576.57  | 222.18 |   524.22  |  393.13 |    0.0    |  0.0  |     0.0     |    0.0     |  0.0   |    0.0     |   0.0   |
| 2026-03-08 |    361.82   |    250.95    |    0.0     |  0.0   | 411.73 |    514.15    |   0.0    |    0.12    |   0.0    |  0.0   |    0.0    |  365.97 |    0.0    |  0.0  |     0.0     |    0.0     |  0.0   |    0.0     |   0.0   |
| 2026-03-07 |    258.15   |     1.97     |    0.0     |  0.0   | 503.1  |    471.62    |   0.0    |    0.0     |  111.02  |  0.0   |    0.0    |  215.58 |    0.0    |  0.0  |     0.0     |    0.0     |  0.0   |    0.0     |   0.0   |
| 2026-03-06 |    241.25   |     1.17     |    0.0     |  0.0   | 277.67 |    128.87    |   0.0    |    0.0     | 1302.88  |  0.0   |    0.0    |   0.0   |    0.0    |  0.0  |     0.0     |    0.0     |  0.0   |    0.0     |   0.0   |
| 2026-03-05 |    404.77   |     2.35     |    0.0     | 238.2  | 764.2  |    109.45    |   0.0    |    0.0     |  474.63  |  0.0   |    0.0    |  828.8  |    0.0    |  0.0  |     0.0     |    0.0     |  0.0   |    0.0     |   0.0   |
| 2026-03-04 |     0.0     |     1.28     |    0.0     |  0.0   | 365.67 |     0.0      |   0.0    |    6.25    |  805.13  |  0.0   |    0.0    |  72.45  |    0.0    |  0.0  |     0.0     |    0.0     |  0.0   |   777.0    |   0.0   |
| 2026-03-03 |     0.0     |     1.08     |    0.0     |  0.0   | 957.27 |    51.08     |   0.0    |   58.68    |  996.68  | 25.82  |    0.0    |   0.0   |    0.0    |  0.0  |     0.0     |    0.0     |  0.0   |   743.15   |   0.0   |
| 2026-03-02 |    74.35    |     1.1      |    0.0     |  0.0   | 440.97 |    30.12     |   0.0    |    0.0     |  800.62  | 266.55 |    0.0    |   0.0   |    0.0    |  0.0  |     0.0     |    0.0     |  0.0   |    0.0     |   0.0   |
| 2026-03-01 |    696.93   |    146.73    |    0.0     |  0.0   | 122.3  |     3.43     |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    |  0.0  |     0.0     |    0.0     |  0.0   |    0.0     |   0.0   |
| 2026-02-28 |    690.27   |     29.1     |    0.0     |  0.0   | 607.97 |    875.08    |   0.0    |    0.0     |  471.03  | 179.65 |    0.0    |   0.0   |   228.98  |  0.0  |     0.0     |    0.0     |  0.0   |    0.0     |   0.0   |
| 2026-02-27 |    335.1    |     0.98     |    0.0     |  0.0   |  0.0   |     0.0      |   0.0    |    0.0     |  525.37  |  0.0   |    0.0    |   0.0   |    0.0    |  0.0  |     0.0     |    0.0     |  0.0   |    0.0     |   0.0   |
| 2026-02-26 |    817.38   |     0.9      |    0.0     |  0.0   | 703.7  |     0.0      |   0.0    |    0.0     |  626.75  |  0.65  |    0.0    |  72.85  |    0.0    |  0.0  |     0.0     |    0.0     |  0.0   |   795.7    |   0.0   |
| 2026-02-25 |    678.8    |    85.32     |    0.0     |  0.0   | 1295.5 |     0.0      |   0.0    |    5.1     |  680.75  | 136.02 |    0.0    |   0.0   |    0.0    |  0.0  |     0.0     |    0.0     |  0.0   |   456.7    |   0.0   |

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
