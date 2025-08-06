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
|  Total  |     102d    |     108d     |    31d     |  30d  |  28d  |     61d      |   23d    |     6d     |   72d    |  12d  |    63d    |   62d   |    39d    | 12d |     11d     |     2d     |  11d   |     6d     |
| 2025-08 |      4      |      6       |     0      |   0   |   0   |      2       |    0     |     0      |    5     |   0   |     1     |    0    |     1     |  0  |      0      |     0      |   0    |     1      |
| 2025-07 |      29     |      29      |     4      |   0   |   4   |      19      |    10    |     0      |    23    |   3   |     19    |    23   |     12    |  2  |      0      |     1      |   11   |     5      |
| 2025-06 |      28     |      28      |     3      |   8   |   6   |      20      |    10    |     0      |    26    |   6   |     11    |    18   |     15    |  7  |      5      |     0      |   0    |     0      |
| 2025-05 |      23     |      26      |     15     |   8   |   9   |      9       |    0     |     3      |    13    |   1   |     19    |    11   |     7     |  2  |      6      |     1      |   0    |     0      |
| 2025-04 |      18     |      19      |     9      |   14  |   9   |      11      |    3     |     3      |    5     |   2   |     13    |    10   |     4     |  1  |      0      |     0      |   0    |     0      |

## Daily login time in minutes for the past 30 days
|    date    | pengbenkang | yangjianchao | pengyinlun | juxin | hello  | shenjunzhong | fengjing | wangjianan | chendong | hejun | yangrenyu | xuezeyu | kangyuhan |  lzd   | yangjingkui | tangminjin | guohui | mashaocong |
|:----------:|:-----------:|:------------:|:----------:|:-----:|:------:|:------------:|:--------:|:----------:|:--------:|:-----:|:---------:|:-------:|:---------:|:------:|:-----------:|:----------:|:------:|:----------:|
|   Total    |    183.0h   |    277.3h    |    7.6h    |  0.0h |  8.7h  |    111.1h    |  84.6h   |    0.0h    |  242.1h  |  1.3h |   133.7h  |  99.4h  |   38.8h   |  3.7h  |     0.0h    |    0.0h    | 22.8h  |   10.6h    |
| 2025-08-06 |     0.0     |     0.57     |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |  877.53  |  0.0  |    0.0    |   0.0   |   134.6   |  0.0   |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-08-05 |     0.0     |     0.63     |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |  881.53  |  0.0  |    0.0    |   0.0   |    0.0    |  0.0   |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-08-04 |    40.77    |     0.52     |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     | 1222.87  |  0.0  |    0.0    |   0.0   |    0.0    |  0.0   |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-08-03 |    315.02   |     0.62     |    0.0     |  0.0  |  0.0   |    38.68     |   0.0    |    0.0     |  638.68  |  0.0  |    0.07   |   0.0   |    0.0    |  0.0   |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-08-02 |    203.05   |     0.58     |    0.0     |  0.0  |  0.0   |    98.03     |   0.0    |    0.0     |   0.0    |  0.0  |    0.0    |   0.0   |    0.0    |  0.0   |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-08-01 |    403.28   |     4.65     |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |  641.57  |  0.0  |    0.0    |   0.0   |    0.0    |  0.0   |     0.0     |    0.0     |  0.0   |    0.6     |
| 2025-07-31 |    139.05   |    16.78     |    0.0     |  0.0  |  0.0   |    425.23    |   0.0    |    0.0     | 1047.62  |  0.0  |   142.22  |  43.67  |    0.0    |  0.0   |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-07-30 |    187.02   |    168.92    |    0.0     |  0.0  |  0.0   |    368.8     |  166.0   |    0.0     |  923.22  |  0.0  |   77.87   |  378.03 |    0.0    |  0.0   |     0.0     |    0.0     |  0.0   |    0.85    |
| 2025-07-29 |     49.5    |    141.13    |    0.0     |  0.0  |  0.0   |    549.23    |  510.48  |    0.0     |  842.12  | 76.28 |    0.0    |  155.77 |    0.0    |  0.0   |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-07-28 |    393.98   |     0.55     |    0.0     |  0.0  |  0.0   |    679.88    |  223.77  |    0.0     |  793.27  |  0.0  |   890.05  |  276.22 |    0.0    |  0.0   |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-07-27 |    515.37   |     0.67     |    0.0     |  0.0  |  0.0   |    116.27    |   0.0    |    0.0     |   0.0    |  0.0  |    0.0    |   0.0   |    0.0    |  0.0   |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-07-26 |    508.03   |     0.58     |    0.0     |  0.0  |  0.0   |    111.0     |   4.62   |    0.0     |  511.97  |  0.0  |    0.0    |   0.0   |    0.0    |  0.0   |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-07-25 |    193.62   |     0.32     |   236.03   |  0.0  |  0.0   |     0.0      |  771.37  |    0.0     |  482.37  |  0.0  |    0.0    |  474.23 |   138.72  |  0.0   |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-07-23 |    401.02   |    542.43    |    0.0     |  0.0  |  0.0   |    530.93    |  500.02  |    0.0     |  886.68  |  0.0  |   697.07  |  324.52 |   254.22  |  0.0   |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-07-22 |    606.62   |    780.88    |   115.05   |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |  755.22  |  0.0  |   574.53  |  349.28 |    0.0    | 118.2  |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-07-21 |    474.17   |    575.73    |   102.28   |  0.0  | 113.3  |    485.27    |   0.0    |    0.0     |  446.02  |  0.0  |   560.98  |  138.08 |    0.0    | 102.73 |     0.0     |    0.0     | 81.72  |    2.45    |
| 2025-07-20 |    589.58   |    100.53    |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |   0.0    |  0.0  |    0.0    |   0.0   |    0.0    |  0.0   |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-07-18 |    521.57   |    766.67    |    0.0     |  0.0  | 28.35  |    257.73    |   0.0    |    0.0     |  159.97  |  0.0  |   240.45  |   0.0   |    0.0    |  0.0   |     0.0     |    0.0     | 98.28  |    0.0     |
| 2025-07-17 |    885.9    |    985.83    |    0.0     |  0.0  |  0.0   |    112.05    |   0.0    |    0.0     |  384.22  |  0.0  |   650.83  |  114.43 |    0.0    |  0.0   |     0.0     |    0.0     | 63.13  |    3.95    |
| 2025-07-16 |    435.7    |   1132.87    |    0.0     |  0.0  |  0.0   |     0.0      |  884.7   |    0.0     |  307.02  |  0.0  |   657.7   |  206.35 |   242.62  |  0.0   |     0.0     |    0.0     | 260.98 |    1.45    |
| 2025-07-15 |    426.05   |    888.05    |    0.0     |  0.0  | 153.17 |    317.6     | 1077.43  |    0.0     |   0.0    |  0.0  |   579.2   | 1016.02 |   310.07  |  0.0   |     0.0     |    0.0     | 182.27 |   627.07   |
| 2025-07-14 |    616.02   |    1000.6    |    0.0     |  0.0  | 228.67 |    523.27    |  937.9   |    0.0     |  858.72  |  0.0  |   588.13  |  319.4  |   352.05  |  0.0   |     0.0     |    0.0     | 108.55 |    0.0     |
| 2025-07-13 |    59.98    |   1168.85    |    0.0     |  0.0  |  0.0   |    290.43    |   0.0    |    0.0     |   1.87   |  0.0  |    0.0    |   0.0   |    0.0    |  0.0   |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-07-12 |    95.77    |   1091.52    |    0.0     |  0.0  |  0.0   |    210.9     |   0.0    |    0.0     |   0.0    |  0.0  |    0.0    |  288.58 |    0.0    |  0.0   |     0.0     |    0.73    |  0.0   |    0.0     |
| 2025-07-11 |    278.9    |   1369.42    |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |  575.2   |  0.0  |   158.08  |  493.25 |   103.52  |  0.0   |     0.0     |    0.0     | 162.87 |    0.0     |
| 2025-07-10 |    456.18   |   1269.08    |    0.0     |  0.0  |  0.0   |     0.0      |   0.0    |    0.0     |  323.05  |  0.0  |   648.78  |  560.67 |   378.37  |  0.0   |     0.0     |    0.0     | 210.12 |    0.0     |
| 2025-07-09 |    532.0    |   1268.48    |    0.0     |  0.0  |  0.0   |    350.52    |   0.0    |    0.0     |  426.4   |  0.0  |   675.97  |  305.47 |   286.48  |  0.0   |     0.0     |    0.0     | 193.72 |    0.0     |
| 2025-07-08 |    704.82   |   1010.88    |    0.0     |  0.0  |  0.0   |    452.92    |   0.0    |    0.0     |  363.58  |  0.0  |   615.75  |  196.27 |   82.88   |  0.0   |     0.0     |    0.0     |  8.03  |    0.0     |
| 2025-07-07 |    494.02   |    1278.7    |    0.0     |  0.0  |  0.0   |    431.07    |   0.0    |    0.0     |  177.5   |  0.0  |   261.75  |  324.95 |   43.98   |  0.0   |     0.0     |    0.0     |  0.0   |    0.0     |
| 2025-07-06 |    455.73   |   1068.02    |    0.0     |  0.0  |  0.0   |    315.83    |   0.0    |    0.0     |   0.0    |  0.0  |    0.0    |   0.0   |    0.0    |  0.0   |     0.0     |    0.0     |  0.0   |    0.0     |

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
