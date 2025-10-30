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
|  Total  |     162d    |     190d     |    37d     |  30d  |  36d  |     109d     |   37d    |    13d     |   135d   |  38d  |    106d   |   95d   |    67d    | 12d |     13d     |     2d     |  11d   |    10d     |
| 2025-10 |      24     |      30      |     5      |   0   |   5   |      15      |    1     |     0      |    20    |   12  |     17    |    13   |     2     |  0  |      0      |     0      |   0    |     0      |
| 2025-09 |      28     |      29      |     0      |   0   |   3   |      12      |    13    |     2      |    23    |   14  |     21    |    6    |     12    |  0  |      1      |     0      |   0    |     3      |
| 2025-08 |      12     |      29      |     1      |   0   |   0   |      23      |    0     |     5      |    25    |   0   |     6     |    14   |     15    |  0  |      1      |     0      |   0    |     2      |
| 2025-07 |      29     |      29      |     4      |   0   |   4   |      19      |    10    |     0      |    23    |   3   |     19    |    23   |     12    |  2  |      0      |     1      |   11   |     5      |
| 2025-06 |      28     |      28      |     3      |   8   |   6   |      20      |    10    |     0      |    26    |   6   |     11    |    18   |     15    |  7  |      5      |     0      |   0    |     0      |
| 2025-05 |      23     |      26      |     15     |   8   |   9   |      9       |    0     |     3      |    13    |   1   |     19    |    11   |     7     |  2  |      6      |     1      |   0    |     0      |
| 2025-04 |      18     |      19      |     9      |   14  |   9   |      11      |    3     |     3      |    5     |   2   |     13    |    10   |     4     |  1  |      0      |     0      |   0    |     0      |

## Daily login time in minutes for the past 30 days
|    date    | pengbenkang | yangjianchao | pengyinlun | juxin | hello  | shenjunzhong | fengjing | wangjianan | chendong | hejun  | yangrenyu | xuezeyu | kangyuhan | lzd | yangjingkui | tangminjin | guohui | mashaocong |
|:----------:|:-----------:|:------------:|:----------:|:-----:|:------:|:------------:|:--------:|:----------:|:--------:|:------:|:---------:|:-------:|:---------:|:---:|:-----------:|:----------:|:------:|:----------:|
|   Total    |    184.2h   |    448.9h    |   31.7h    |  0.0h | 18.4h  |    64.8h     |  14.6h   |    0.0h    |  160.3h  | 53.2h  |   152.7h  |  67.5h  |    1.5h   | 0.0h |     0.0h    |    0.0h    |  0.0h  |    0.0h    |
| 2025-10-30 |    343.07   |   1344.77    |    0.0     |  0.0  |  0.0   |     45.5     |   0.0    |    0.0     |  300.92  | 345.12 |   996.85  |  157.4  |   14.92   | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-10-29 |    382.97   |   1243.13    |    0.0     |  0.0  | 56.52  |    320.63    |   0.0    |    0.0     |  669.58  |  0.0   |   884.17  |  148.33 |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-10-28 |    524.4    |    672.42    |   350.6    |  0.0  |  0.0   |    423.42    |   0.0    |    0.0     |  371.1   | 227.75 |   869.1   |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-10-27 |    567.7    |    908.6     |    0.0     |  0.0  | 235.07 |    449.07    |   0.0    |    0.0     |  528.68  | 89.92  |   633.58  |  310.58 |   74.93   | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-10-26 |     0.0     |    950.6     |    0.0     |  0.0  |  0.0   |    344.45    |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |  89.37  |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-10-25 |    355.22   |   1049.72    |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |  350.47  |  0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-10-24 |    162.12   |    692.43    |   263.93   |  0.0  | 273.4  |    142.18    |   0.0    |    0.0     |  491.53  |  0.0   |   502.87  |  911.03 |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-10-23 |    378.78   |   1184.97    |   291.08   |  0.0  | 379.18 |    106.93    |   0.0    |    0.0     |  516.25  | 14.85  |   856.1   |  540.67 |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-10-22 |    455.03   |    885.6     |    0.0     |  0.0  | 160.2  |     0.0      |   0.0    |    0.0     |  735.83  | 631.18 |   817.65  |  504.68 |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-10-21 |    922.92   |    893.08    |   935.05   |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |  39.97   |  0.0   |   916.5   |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-10-20 |    509.28   |   1058.72    |   60.15    |  0.0  |  0.0   |    154.77    |   0.0    |    0.0     |  659.1   |  0.0   |   444.17  |  145.78 |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-10-19 |    409.1    |    37.57     |    0.0     |  0.0  |  0.0   |    292.23    |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-10-18 |    437.27   |    423.42    |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |  480.33  |  0.0   |    0.0    |  554.05 |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-10-17 |    131.13   |   1410.52    |    0.0     |  0.0  |  0.0   |     50.1     |   0.0    |    0.0     |  512.88  |  0.0   |   152.23  |  155.9  |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-10-16 |    691.03   |   1151.13    |    0.0     |  0.0  |  0.0   |    244.53    |   0.0    |    0.0     |  862.12  |  0.0   |   313.58  |  344.53 |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-10-15 |    531.43   |    649.73    |    0.0     |  0.0  |  0.0   |    311.98    |   0.0    |    0.0     |  849.97  | 520.87 |   257.82  |  161.98 |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-10-14 |    492.68   |   1424.55    |    0.0     |  0.0  |  0.0   |    530.55    |   0.0    |    0.0     |  844.78  | 446.2  |   268.02  |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-10-13 |    542.07   |    913.27    |    0.0     |  0.0  |  0.0   |    224.7     |   0.0    |    0.0     |  408.85  | 196.83 |   803.23  |  24.87  |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-10-12 |    625.57   |     0.65     |    0.0     |  0.0  |  0.0   |     0.0      |  878.88  |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-10-11 |    457.93   |    882.15    |    0.0     |  0.0  |  0.0   |    247.85    |   0.0    |    0.0     |  12.47   | 415.62 |   81.63   |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-10-10 |    568.85   |   1060.12    |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |  459.68  |  0.0   |   139.82  |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-10-09 |    479.5    |   1203.62    |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |  513.72  | 51.57  |   223.15  |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-10-08 |     0.0     |   1261.68    |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  97.7  |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-10-07 |     0.0     |    656.85    |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-10-06 |     0.0     |    837.5     |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    | 154.85 |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-10-05 |     0.0     |    615.47    |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-10-04 |     0.0     |    860.17    |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-10-03 |    301.87   |    992.97    |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |   7.18   |  0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-10-02 |    306.78   |    1095.8    |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-10-01 |    475.47   |    571.7     |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |

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
