import math

n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))

dp = [math.inf] * (m + 1)

for i in arr:
    dp[i] = 1

for i in range(1, m + 1):
    for j in arr:
        if dp[i - j] != math.inf and i - j > 0:
            dp[i] = min(dp[i], dp[i - j] + 1)

if dp[m] != math.inf:
    print(dp[m])
else:
    print(-1)
