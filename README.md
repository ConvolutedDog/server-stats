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
|  Total  |     182d    |     210d     |    41d     |  30d  |  43d  |     120d     |   39d    |    13d     |   145d   |  46d  |    119d   |   109d  |    72d    | 12d |     13d     |     4d     |  11d   |    19d     |
| 2025-11 |      19     |      19      |     4      |   0   |   7   |      10      |    2     |     0      |    9     |   8   |     12    |    13   |     5     |  0  |      0      |     2      |   0    |     9      |
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
|   Total    |    264.0h   |    433.3h    |   45.7h    |  0.0h | 42.2h  |    69.3h     |  22.5h   |    0.0h    |  117.3h  | 71.7h  |   263.0h  |  87.6h  |   26.5h   | 0.0h |     0.0h    |    3.2h    |  0.0h  |   29.6h    |
| 2025-11-19 |    841.32   |    1060.0    |    0.0     |  0.0  | 108.32 |     0.0      |   0.0    |    0.0     |  580.83  | 511.97 |   891.3   |  11.32  |   532.97  | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-11-18 |    863.58   |    756.88    |   384.73   |  0.0  | 345.18 |     0.0      |   0.0    |    0.0     |  395.58  | 710.07 |   817.0   |   0.0   |   601.8   | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-11-17 |    832.3    |    178.87    |    0.0     |  0.0  | 365.82 |     0.0      |   0.0    |    0.0     |   0.0    |  0.4   |   808.47  |  275.33 |    0.43   | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-11-16 |    897.2    |   1199.98    |    0.0     |  0.0  |  0.0   |    84.12     |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |  103.05 |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |   489.63   |
| 2025-11-15 |    539.97   |    664.5     |    0.0     |  0.0  |  0.0   |    477.58    |   0.0    |    0.0     |  90.37   |  0.0   |    0.0    |  139.5  |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |   195.87   |
| 2025-11-14 |   1307.23   |   1309.02    |   70.78    |  0.0  | 116.48 |    200.2     |   0.0    |    0.0     |  235.32  | 97.83  |   806.48  |  124.73 |   287.23  | 0.0 |     0.0     |    0.0     |  0.0   |   450.77   |
| 2025-11-13 |    539.0    |    838.42    |   246.15   |  0.0  | 444.95 |    43.43     |   0.0    |    0.0     |   0.0    |  0.0   |   797.45  |  294.9  |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |   458.3    |
| 2025-11-12 |    152.27   |    341.87    |    0.0     |  0.0  |  0.0   |    130.42    |   0.0    |    0.0     |   0.0    |  0.0   |   311.2   |  228.52 |   78.03   | 0.0 |     0.0     |    0.0     |  0.0   |   175.42   |
| 2025-11-11 |    525.75   |    567.23    |    0.0     |  0.0  |  0.0   |    26.25     |   0.0    |    0.0     |   0.0    |  0.0   |   656.6   |  639.95 |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.6     |
| 2025-11-10 |    578.82   |    945.08    |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |  277.15  |  0.0   |   841.78  |  332.87 |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.47    |
| 2025-11-09 |    568.28   |    724.4     |    0.0     |  0.0  |  0.0   |    231.17    |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-11-08 |    555.98   |    916.18    |    0.0     |  0.0  |  0.0   |    299.38    |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |  133.05 |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.43    |
| 2025-11-07 |    537.53   |    1362.3    |    0.0     |  0.0  |  0.0   |    535.53    |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-11-06 |    499.85   |   1249.63    |    0.0     |  0.0  | 44.92  |     0.0      |   0.0    |    0.0     |  619.83  | 165.8  |   904.85  |  41.67  |    0.0    | 0.0 |     0.0     |   193.42   |  0.0   |    2.52    |
| 2025-11-05 |    334.78   |    954.03    |    0.0     |  0.0  |  0.0   |     0.0      |  480.67  |    0.0     |  10.67   | 226.22 |   174.87  |  104.05 |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-11-04 |    377.88   |    606.45    |   200.18   |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |  512.63  | 619.12 |  1041.15  |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-11-03 |    491.0    |    875.52    |    0.0     |  0.0  |  0.8   |    164.43    |  869.82  |    0.0     |   0.0    | 659.48 |   661.83  |   0.0   |    0.0    | 0.0 |     0.0     |    0.05    |  0.0   |    0.0     |
| 2025-11-02 |    385.75   |    308.82    |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |  308.62  |  0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-11-01 |    516.68   |    846.55    |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0   |    0.0    |  64.35  |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-10-31 |    399.77   |    464.82    |    0.0     |  0.0  |  0.0   |    136.23    |   0.0    |    0.0     |   4.07   |  0.0   |   589.45  |  97.95  |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
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
