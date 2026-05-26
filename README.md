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
|  month  | pengbenkang | yangjianchao | pengyinlun | juxin | hello | shenjunzhong | fengjing | wangjianan | chendong | hejun | yangrenyu | xuezeyu | kangyuhan | lzd | yangjingkui | tangminjin | guohui | mashaocong | shiyang | yuanpiao | zhouluchen | xzy | dengcan | tangzhongyi |
|:-------:|:-----------:|:------------:|:----------:|:-----:|:-----:|:------------:|:--------:|:----------:|:--------:|:-----:|:---------:|:-------:|:---------:|:---:|:-----------:|:----------:|:------:|:----------:|:-------:|:--------:|:----------:|:---:|:-------:|:-----------:|
|  Total  |     315d    |     391d     |    99d     |  46d  |  185d |     233d     |   142d   |    37d     |   251d   |  111d |    229d   |   204d  |    112d   | 23d |     13d     |     4d     |  11d   |    79d     |    2d   |   23d    |     1d     | 21d |    6d   |      3d     |
| 2026-05 |      11     |      25      |     6      |   3   |   24  |      7       |    18    |     0      |    1     |   3   |     18    |    13   |     15    |  2  |      0      |     0      |   0    |     12     |    0    |    6     |     0      |  8  |    0    |      0      |
| 2026-04 |      23     |      30      |     15     |   1   |   27  |      23      |    24    |     0      |    9     |   5   |     24    |    24   |     0     |  4  |      0      |     0      |   0    |     22     |    0    |    16    |     0      |  12 |    6    |      3      |
| 2026-03 |      20     |      31      |     15     |   9   |   28  |      23      |    11    |     13     |    17    |   10  |     15    |    26   |     7     |  5  |      0      |     0      |   0    |     2      |    2    |    1     |     1      |  1  |    0    |      0      |
| 2026-02 |      24     |      26      |     0      |   1   |   9   |      10      |    4     |     11     |    24    |   9   |     5     |    7    |     4     |  0  |      0      |     0      |   0    |     13     |    0    |    0     |     0      |  0  |    0    |      0      |
| 2026-01 |      18     |      29      |     10     |   1   |   26  |      27      |    23    |     0      |    21    |   19  |     20    |    20   |     12    |  0  |      0      |     0      |   0    |     6      |    0    |    0     |     0      |  0  |    0    |      0      |
| 2025-12 |      27     |      29      |     8      |   0   |   21  |      18      |    19    |     0      |    24    |   14  |     22    |    5    |     2     |  0  |      0      |     0      |   0    |     3      |    0    |    0     |     0      |  0  |    0    |      0      |
| 2025-11 |      29     |      30      |     8      |   1   |   14  |      15      |    6     |     0      |    19    |   13  |     18    |    13   |     5     |  0  |      0      |     2      |   0    |     11     |    0    |    0     |     0      |  0  |    0    |      0      |
| 2025-10 |      25     |      31      |     5      |   0   |   5   |      16      |    1     |     0      |    21    |   12  |     18    |    14   |     2     |  0  |      0      |     0      |   0    |     0      |    0    |    0     |     0      |  0  |    0    |      0      |
| 2025-09 |      28     |      29      |     0      |   0   |   3   |      12      |    13    |     2      |    23    |   14  |     21    |    6    |     12    |  0  |      1      |     0      |   0    |     3      |    0    |    0     |     0      |  0  |    0    |      0      |
| 2025-08 |      12     |      29      |     1      |   0   |   0   |      23      |    0     |     5      |    25    |   0   |     6     |    14   |     15    |  0  |      1      |     0      |   0    |     2      |    0    |    0     |     0      |  0  |    0    |      0      |
| 2025-07 |      29     |      29      |     4      |   0   |   4   |      19      |    10    |     0      |    23    |   3   |     19    |    23   |     12    |  2  |      0      |     1      |   11   |     5      |    0    |    0     |     0      |  0  |    0    |      0      |
| 2025-06 |      28     |      28      |     3      |   8   |   6   |      20      |    10    |     0      |    26    |   6   |     11    |    18   |     15    |  7  |      5      |     0      |   0    |     0      |    0    |    0     |     0      |  0  |    0    |      0      |
| 2025-05 |      23     |      26      |     15     |   8   |   9   |      9       |    0     |     3      |    13    |   1   |     19    |    11   |     7     |  2  |      6      |     1      |   0    |     0      |    0    |    0     |     0      |  0  |    0    |      0      |
| 2025-04 |      18     |      19      |     9      |   14  |   9   |      11      |    3     |     3      |    5     |   2   |     13    |    10   |     4     |  1  |      0      |     0      |   0    |     0      |    0    |    0     |     0      |  0  |    0    |      0      |

## Daily login time in minutes for the past 30 days
|    date    | pengbenkang | yangjianchao | pengyinlun | juxin  | hello  | shenjunzhong | fengjing | wangjianan | chendong | hejun  | yangrenyu | xuezeyu | kangyuhan |  lzd  | yangjingkui | tangminjin | guohui | mashaocong | shiyang | yuanpiao | zhouluchen |  xzy   | dengcan | tangzhongyi |
|:----------:|:-----------:|:------------:|:----------:|:------:|:------:|:------------:|:--------:|:----------:|:--------:|:------:|:---------:|:-------:|:---------:|:-----:|:-----------:|:----------:|:------:|:----------:|:-------:|:--------:|:----------:|:------:|:-------:|:-----------:|
|   Total    |    94.8h    |    301.5h    |   50.4h    |  8.5h  | 293.5h |    48.2h     |  255.5h  |    0.0h    |   0.4h   |  5.5h  |   197.9h  |  205.3h |   46.2h   |  4.2h |     0.0h    |    0.0h    |  0.0h  |   104.8h   |   0.0h  |  28.6h   |    0.0h    | 37.7h  |   0.0h  |     0.0h    |
| 2026-05-26 |     0.0     |    36.37     |    0.0     |  0.0   | 338.72 |     0.0      | 1429.42  |    0.0     |   0.0    |  0.0   |   836.43  |  835.23 |   72.45   |  0.0  |     0.0     |    0.0     |  0.0   |    0.0     |   0.0   |   0.0    |    0.0     |  0.0   |   0.0   |     0.0     |
| 2026-05-25 |    11.58    |     0.72     |    0.0     |  0.0   | 810.77 |     0.0      |  895.05  |    0.0     |   0.0    |  0.0   |   550.52  |  613.58 |    0.0    |  0.0  |     0.0     |    0.0     |  0.0   |    0.0     |   0.0   |  54.52   |    0.0     |  0.0   |   0.0   |     0.0     |
| 2026-05-24 |    183.55   |     0.0      |    0.0     |  0.0   | 357.18 |     0.0      |  625.9   |    0.0     |   0.0    |  0.0   |    0.0    | 1363.22 |    0.0    |  0.0  |     0.0     |    0.0     |  0.0   |    0.0     |   0.0   |   0.0    |    0.0     |  0.0   |   0.0   |     0.0     |
| 2026-05-23 |     0.0     |     0.67     |    0.0     |  0.0   | 424.63 |     0.0      |  702.28  |    0.0     |   0.0    |  0.0   |    0.0    |  508.82 |   17.37   |  0.0  |     0.0     |    0.0     |  0.0   |    0.0     |   0.0   |   0.0    |    0.0     |  0.0   |   0.0   |     0.0     |
| 2026-05-22 |     0.0     |    267.18    |    0.0     |  0.0   | 292.65 |     0.0      |  434.53  |    0.0     |   0.0    |  0.0   |    0.0    |  401.4  |    0.0    |  0.0  |     0.0     |    0.0     |  0.0   |    0.0     |   0.0   |   0.0    |    0.0     |  0.35  |   0.0   |     0.0     |
| 2026-05-21 |     0.0     |     0.73     |   25.52    |  0.0   | 876.17 |     0.0      |  561.07  |    0.0     |   0.0    |  0.0   |   562.73  |   0.0   |   196.4   |  0.0  |     0.0     |    0.0     |  0.0   |    0.05    |   0.0   |   0.0    |    0.0     | 112.67 |   0.0   |     0.0     |
| 2026-05-20 |     0.0     |    586.03    |   425.45   | 41.93  | 370.35 |     0.0      |  803.9   |    0.0     |   0.0    | 166.95 |   728.93  |   0.0   |    0.0    |  0.0  |     0.0     |    0.0     |  0.0   |   545.58   |   0.0   |   0.0    |    0.0     | 152.73 |   0.0   |     0.0     |
| 2026-05-19 |     0.0     |   1326.77    |    0.0     | 311.07 | 819.05 |     0.0      |  613.82  |    0.0     |   21.9   | 159.02 |   548.3   |   0.0   |   197.03  |  0.0  |     0.0     |    0.0     |  0.0   |    0.0     |   0.0   |   0.0    |    0.0     |  0.0   |   0.0   |     0.0     |
| 2026-05-18 |     0.0     |   1373.58    |    0.0     |  0.0   | 865.25 |    153.87    |   0.0    |    0.0     |   0.0    |  4.12  |   499.83  |  958.42 |   425.65  |  0.0  |     0.0     |    0.0     |  0.0   |    0.0     |   0.0   |   0.0    |    0.0     |  7.17  |   0.0   |     0.0     |
| 2026-05-17 |     3.22    |   1115.78    |    0.0     |  0.0   | 585.08 |    497.73    |  892.92  |    0.0     |   0.0    |  0.0   |    0.0    | 1324.03 |    80.2   |  0.0  |     0.0     |    0.0     |  0.0   |    23.7    |   0.0   |   0.0    |    0.0     |  0.0   |   0.0   |     0.0     |
| 2026-05-16 |     0.0     |   1434.98    |    0.0     |  0.0   | 804.28 |    725.33    |  769.38  |    0.0     |   0.0    |  0.0   |    0.0    |  63.47  |    0.0    |  0.0  |     0.0     |    0.0     |  0.0   |    0.0     |   0.0   |   0.0    |    0.0     |  0.0   |   0.0   |     0.0     |
| 2026-05-15 |     1.5     |    1359.6    |    0.0     |  0.0   | 860.87 |    244.4     |   0.0    |    0.0     |   0.0    |  0.0   |   326.18  |   0.0   |    90.5   |  0.0  |     0.0     |    0.0     |  0.0   |   854.02   |   0.0   |   0.0    |    0.0     |  0.0   |   0.0   |     0.0     |
| 2026-05-14 |     0.0     |    683.58    |   379.48   |  0.0   | 750.73 |    94.07     |  707.35  |    0.0     |   0.0    |  0.0   |   613.4   |  396.77 |   331.62  |  0.0  |     0.0     |    0.0     |  0.0   |   551.12   |   0.0   |  10.18   |    0.0     | 484.8  |   0.0   |     0.0     |
| 2026-05-13 |     7.38    |    1237.8    |    0.0     |  0.0   | 519.67 |     0.0      |  941.07  |    0.0     |   0.0    |  0.0   |   768.22  |  1429.2 |   263.62  |  0.0  |     0.0     |    0.0     |  0.0   |    0.0     |   0.0   |   0.0    |    0.0     | 322.92 |   0.0   |     0.0     |
| 2026-05-12 |     0.0     |   1265.02    |    0.0     |  0.0   | 685.77 |    212.45    |  385.37  |    0.0     |   0.0    |  0.0   |   574.05  |  408.05 |   255.25  |  0.0  |     0.0     |    0.0     |  0.0   |    0.0     |   0.0   |  343.73  |    0.0     |  0.0   |   0.0   |     0.0     |
| 2026-05-11 |     0.0     |   1012.98    |    0.0     |  0.0   | 822.27 |    280.25    |   0.0    |    0.0     |   0.0    |  0.0   |   510.4   |   0.0   |   100.75  |  0.0  |     0.0     |    0.0     |  0.0   |   23.82    |   0.0   |   0.0    |    0.0     |  0.0   |   0.0   |     0.0     |
| 2026-05-10 |     0.0     |   1127.62    |   868.43   |  0.0   | 726.03 |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |   435.5   |   0.0   |    0.0    |  0.0  |     0.0     |    0.0     |  0.0   |   108.32   |   0.0   |   0.0    |    0.0     |  0.0   |   0.0   |     0.0     |
| 2026-05-09 |     0.0     |    759.38    |    0.0     |  0.0   | 656.05 |     0.0      |  712.18  |    0.0     |   0.0    |  0.0   |   315.18  |   0.0   |   15.83   |  0.37 |     0.0     |    0.0     |  0.0   |    0.0     |   0.0   |   0.0    |    0.0     |  0.0   |   0.0   |     0.0     |
| 2026-05-08 |     0.0     |    838.85    |    0.0     |  0.0   | 712.35 |     0.0      |  93.17   |    0.0     |   0.0    |  0.0   |   527.98  |   0.0   |    85.5   |  0.0  |     0.0     |    0.0     |  0.0   |    0.0     |   0.0   |   0.0    |    0.0     | 266.15 |   0.0   |     0.0     |
| 2026-05-07 |     0.0     |   1166.55    |   931.63   |  0.0   | 857.13 |     0.0      |  977.03  |    0.0     |   0.0    |  0.0   |   932.53  | 1318.12 |    0.0    |  0.0  |     0.0     |    0.0     |  0.0   |   199.37   |   0.0   |   0.0    |    0.0     | 738.58 |   0.0   |     0.0     |
| 2026-05-06 |    349.42   |    826.53    |   87.57    | 157.97 | 417.55 |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |   528.9   |  725.32 |   319.28  | 49.05 |     0.0     |    0.0     |  0.0   |    0.0     |   0.0   |  156.83  |    0.0     |  0.0   |   0.0   |     0.0     |
| 2026-05-05 |    483.4    |     1.55     |    0.0     |  0.0   |  0.0   |     0.0      | 1032.97  |    0.0     |   0.0    |  0.0   |   815.28  |   0.0   |   320.9   |  0.0  |     0.0     |    0.0     |  0.0   |   706.95   |   0.0   |  68.12   |    0.0     |  0.0   |   0.0   |     0.0     |
| 2026-05-04 |    574.57   |    74.35     |    0.0     |  0.0   | 457.5  |     0.0      |  432.87  |    0.0     |   0.0    |  0.0   |   278.05  |   0.0   |    0.0    |  0.0  |     0.0     |    0.0     |  0.0   |   607.1    |   0.0   |  135.0   |    0.0     |  0.0   |   0.0   |     0.0     |
| 2026-05-03 |    167.67   |     2.67     |    0.0     |  0.0   | 208.08 |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    |  0.0  |     0.0     |    0.0     |  0.0   |    0.0     |   0.0   |   0.0    |    0.0     |  0.0   |   0.0   |     0.0     |
| 2026-05-02 |    811.98   |    534.82    |    0.0     |  0.0   | 20.05  |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    |  0.0  |     0.0     |    0.0     |  0.0   |  1406.38   |   0.0   |   0.0    |    0.0     |  0.0   |   0.0   |     0.0     |
| 2026-05-01 |    779.13   |    26.28     |    0.0     |  0.0   |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    |  0.0  |     0.0     |    0.0     |  0.0   |    7.13    |   0.0   |   0.0    |    0.0     |  0.0   |   0.0   |     0.0     |
| 2026-04-30 |    631.8    |    778.12    |    0.0     |  0.0   | 845.05 |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |   229.8   |  692.18 |    0.0    |  0.0  |     0.0     |    0.0     |  0.0   |    0.0     |   0.0   |   0.0    |    0.0     |  0.0   |   0.0   |     0.0     |
| 2026-04-29 |    411.22   |    139.93    |    0.0     |  0.0   | 850.85 |     0.0      |  554.63  |    0.0     |   0.0    |  0.0   |   423.57  |  586.48 |    0.0    | 205.4 |     0.0     |    0.0     |  0.0   |   383.85   |   0.0   |  341.35  |    0.0     | 177.12 |   0.0   |     0.0     |
| 2026-04-28 |    622.65   |    107.55    |    0.0     |  0.0   | 847.72 |    683.43    |  908.3   |    0.0     |   0.0    |  0.0   |   548.25  |   0.0   |    0.0    |  0.0  |     0.0     |    0.0     |  0.0   |    0.0     |   0.0   |  53.77   |    0.0     |  0.0   |   0.0   |     0.0     |
| 2026-04-27 |    650.7    |     1.15     |   304.55   |  0.0   | 827.98 |     0.0      |  856.5   |    0.0     |   0.0    |  0.0   |   320.95  |  692.18 |    0.0    |  0.0  |     0.0     |    0.0     |  0.0   |   871.42   |   0.0   |  555.1   |    0.0     |  0.0   |   0.0   |     0.0     |

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
