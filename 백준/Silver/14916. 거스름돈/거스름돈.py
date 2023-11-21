import sys

x = int(sys.stdin.readline())

#     0    1  2   3  4  5
dp = [-1, -1, 1, -1, 2, 1]

for i in range(6, x + 1):
    dp.append(100001)

for i in range(6, x + 1):
    if dp[i - 2] == -1 and dp[i - 5] == -1:
        dp[i] = -1
    elif dp[i - 2] == -1:
        dp[i] = dp[i - 5] + 1
    elif dp[i - 5] == -1:
        dp[i] = dp[i - 2] + 1
    else:
        dp[i] = min(dp[i - 2], dp[i - 5]) + 1

print(dp[x])