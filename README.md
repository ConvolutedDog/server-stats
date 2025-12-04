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
|  Total  |     196d    |     225d     |    46d     |  31d  |  54d  |     126d     |   46d    |    13d     |   159d   |  54d  |    129d   |   110d  |    72d    | 12d |     13d     |     4d     |  11d   |    23d     |
| 2025-12 |      4      |      4       |     1      |   0   |   4   |      1       |    3     |     0      |    4     |   3   |     4     |    1    |     0     |  0  |      0      |     0      |   0    |     2      |
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
|   Total    |    260.9h   |    399.6h    |   25.9h    |  0.0h | 62.4h  |    49.7h     |  55.1h   |    0.0h    |  185.5h  |  79.3h  |   238.7h  |  41.8h  |   25.0h   | 0.0h |     0.0h    |    3.2h    |  0.0h  |   64.4h    |
| 2025-12-04 |    196.58   |    476.17    |    0.0     |  0.0  | 225.87 |     0.0      |  644.78  |    0.0     |  823.15  |  513.3  |   639.75  |  81.47  |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-12-03 |    336.48   |    568.73    |    0.0     |  0.0  | 241.78 |    101.63    |  368.58  |    0.0     |  858.47  | 1324.78 |   900.83  |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |  1364.35   |
| 2025-12-02 |    404.98   |   1311.92    |   48.78    |  0.0  | 97.42  |     0.0      |   0.0    |    0.0     |  823.15  |   0.0   |   806.82  |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |   719.27   |
| 2025-12-01 |    270.97   |    810.53    |    0.0     |  0.0  | 155.82 |     0.0      |  359.23  |    0.0     |  451.45  |  250.07 |   690.78  |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-11-30 |     0.0     |    601.5     |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |   0.15   |   0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-11-29 |    332.57   |   1212.75    |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |  675.75  |   0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    3.98    |
| 2025-11-28 |    243.95   |   1210.25    |    0.0     |  0.0  | 58.95  |     0.0      |   0.0    |    0.0     |  864.22  |  133.43 |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-11-27 |    195.45   |    953.23    |    0.0     |  0.0  | 236.72 |    417.73    |  485.83  |    0.0     |  880.95  |  510.22 |   514.27  |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-11-26 |    182.7    |   1206.18    |   110.27   |  0.07 | 154.88 |    318.95    |   0.0    |    0.0     |  873.18  |  138.43 |   791.58  |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-11-25 |    189.18   |    508.7     |   391.77   |  0.0  | 127.4  |    70.97     |   0.0    |    0.0     |  873.33  |  25.57  |   597.67  |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-11-24 |    785.85   |    773.0     |   41.23    |  0.0  | 371.67 |     0.0      |   0.0    |    0.0     |  547.82  |  149.05 |   791.77  |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.35    |
| 2025-11-23 |    636.45   |     0.87     |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |   0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-11-22 |    304.23   |     0.9      |    0.0     |  0.0  |  0.0   |     1.77     |  862.92  |    0.0     |   2.32   |   0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-11-21 |   1225.15   |    348.5     |   259.52   |  0.0  | 228.07 |    41.52     |   0.03   |    0.0     |  500.27  |   0.0   |   738.02  |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-11-20 |    778.58   |    925.05    |    0.0     |  0.0  | 420.7  |     0.0      |  102.62  |    0.0     |  744.88  |   0.0   |   841.3   |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-11-19 |    841.32   |    1060.0    |    0.0     |  0.0  | 108.32 |     0.0      |   0.0    |    0.0     |  580.83  |  511.97 |   891.3   |  11.32  |   532.97  | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-11-18 |    863.58   |    756.88    |   384.73   |  0.0  | 345.18 |     0.0      |   0.0    |    0.0     |  395.58  |  710.07 |   817.0   |   0.0   |   601.8   | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-11-17 |    832.3    |    178.87    |    0.0     |  0.0  | 365.82 |     0.0      |   0.0    |    0.0     |   0.0    |   0.4   |   808.47  |  275.33 |    0.43   | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-11-16 |    897.2    |   1199.98    |    0.0     |  0.0  |  0.0   |    84.12     |   0.0    |    0.0     |   0.0    |   0.0   |    0.0    |  103.05 |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |   489.63   |
| 2025-11-15 |    539.97   |    664.5     |    0.0     |  0.0  |  0.0   |    477.58    |   0.0    |    0.0     |  90.37   |   0.0   |    0.0    |  139.5  |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |   195.87   |
| 2025-11-14 |   1307.23   |   1309.02    |   70.78    |  0.0  | 116.48 |    200.2     |   0.0    |    0.0     |  235.32  |  97.83  |   806.48  |  124.73 |   287.23  | 0.0 |     0.0     |    0.0     |  0.0   |   450.77   |
| 2025-11-13 |    539.0    |    838.42    |   246.15   |  0.0  | 444.95 |    43.43     |   0.0    |    0.0     |   0.0    |   0.0   |   797.45  |  294.9  |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |   458.3    |
| 2025-11-12 |    152.27   |    341.87    |    0.0     |  0.0  |  0.0   |    130.42    |   0.0    |    0.0     |   0.0    |   0.0   |   311.2   |  228.52 |   78.03   | 0.0 |     0.0     |    0.0     |  0.0   |   175.42   |
| 2025-11-11 |    525.75   |    567.23    |    0.0     |  0.0  |  0.0   |    26.25     |   0.0    |    0.0     |   0.0    |   0.0   |   656.6   |  639.95 |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.6     |
| 2025-11-10 |    578.82   |    945.08    |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |  277.15  |   0.0   |   841.78  |  332.87 |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.47    |
| 2025-11-09 |    568.28   |    724.4     |    0.0     |  0.0  |  0.0   |    231.17    |   0.0    |    0.0     |   0.0    |   0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-11-08 |    555.98   |    916.18    |    0.0     |  0.0  |  0.0   |    299.38    |   0.0    |    0.0     |   0.0    |   0.0   |    0.0    |  133.05 |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.43    |
| 2025-11-07 |    537.53   |    1362.3    |    0.0     |  0.0  |  0.0   |    535.53    |   0.0    |    0.0     |   0.0    |   0.0   |    0.0    |   0.0   |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-11-06 |    499.85   |   1249.63    |    0.0     |  0.0  | 44.92  |     0.0      |   0.0    |    0.0     |  619.83  |  165.8  |   904.85  |  41.67  |    0.0    | 0.0 |     0.0     |   193.42   |  0.0   |    2.52    |
| 2025-11-05 |    334.78   |    954.03    |    0.0     |  0.0  |  0.0   |     0.0      |  480.67  |    0.0     |  10.67   |  226.22 |   174.87  |  104.05 |    0.0    | 0.0 |     0.0     |    0.0     |  0.0   |    0.0     |

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
