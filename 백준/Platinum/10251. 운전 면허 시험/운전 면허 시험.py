t = int(input())
import sys

input = sys.stdin.readline
inf = float('inf')

for _ in range(t):
    m, n, l, g = map(int, input().split())

    width = [list(map(int, input().split())) for _ in range(m)]

    height = [list(map(int, input().split())) for _ in range(m - 1)]
    max_turn = min(n, m) * 2 + 1
    dp = [[[[inf] * n for _ in range(m)] for _ in range(2)] for _ in range(max_turn)]

    # dir 1 = left - right dir 0 up down
    dp[0][1][0][0] = 0
    dp[0][0][0][0] = 0
    dp[1][0][0][0] = 0
    dp[1][1][0][0] = 0

    dp[0][1][1][0] = height[0][0]

    dp[0][0][0][1] = width[0][0]

    for i in range(1, m):
        dp[1][1][i][0] = dp[1][1][i - 1][0] + height[i - 1][0]
        # dp[0][0][i][0] = dp[0][1][i - 1][0] + height[i - 1][0]
    for j in range(1, n):
        # dp[0][1][0][j] = dp[0][1][0][j - 1] + width[0][j - 1]
        dp[1][0][0][j] = dp[1][0][0][j - 1] + width[0][j - 1]
    #
    for i in range(1, m):
        for j in range(1, n):
            for k in range(1, max_turn):
                # dp[k + 1][0][i][j] = min(dp[k][1][i - 1][j] + height[i - 1][j], dp[k + 1][0][i][j])
                # dp[k + 1][1][i][j] = min(dp[k][0][i][j - 1] + width[i][j - 1], dp[k + 1][0][i][j])
                # dp[k][0][i][j] = min(dp[k][0][i - 1][j] + height[i - 1][j], dp[k][0][i][j])
                # dp[k][1][i][j] = min(dp[k][1][i][j - 1] + width[i][j - 1], dp[k][1][i][j])

                dp[k][0][i][j] = min(dp[k - 1][1][i - 1][j], dp[k][0][i - 1][j]) + height[i - 1][j]
                dp[k][1][i][j] = min(dp[k - 1][0][i][j - 1], dp[k][1][i][j - 1]) + width[i][j - 1]
    ans = inf
    for k in range(max_turn):
        if dp[k][0][m - 1][n - 1] <= g:
            ans = min(ans, (n - 1) * l + (m - 1) * l + k)

        if dp[k][1][m - 1][n - 1] <= g:
            ans = min(ans, (n - 1) * l + (m - 1) * l + k)
    print(ans) if ans < inf else print(-1)
