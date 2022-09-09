n, m = map(int, input().split())
import sys

input = sys.stdin.readline
inf = -2e9
arr = [[inf] * (m + 2) for _ in range(n + 1)]

for i in range(n):
    lst = list(map(int, input().split()))
    for j, k in enumerate(lst):
        arr[i + 1][j + 1] = k
left = [[inf] * (m + 2) for _ in range(n + 1)]
right = [[inf] * (m + 2) for _ in range(n + 1)]
i = 1
dp = [[inf] * (m + 2) for _ in range(n + 1)]

for j in range(1, m + 1):
    if j == 1:
        left[i][j] = arr[i][j]
        right[i][j] = arr[i][j]
        dp[i][j] = arr[i][j]

    else:

        left[i][j] = left[i][j - 1] + arr[i][j]
        right[i][j] = right[i][j - 1] + arr[i][j]
        dp[i][j] = dp[i][j - 1] + arr[i][j]

for i in range(2, n + 1):
    for j in range(1, m + 1):
        left[i][j] = max(dp[i - 1][j], left[i][j - 1]) + arr[i][j]

    for j in range(1, m + 1):
        right[i][m-j+1] = max(dp[i - 1][m - j + 1], right[i][m - j + 2]) + arr[i][m-j+1]
    for j in range(1, m + 1):
        dp[i][j] = max(left[i][j], right[i][j])

print(dp[n][m])
