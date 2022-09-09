n = int(input())
street = [list(map(int, input().split())) for i in range(n)]

dp = [[0] * 3 for _ in range(n)]
dp[0][:] = street[0][:]

for i in range(1, n):
    dp[i][0] = min(dp[i - 1][1] + street[i][0], dp[i - 1][2] + street[i][0])
    dp[i][1] = min(dp[i - 1][0] + street[i][1], dp[i - 1][2] + street[i][1])
    dp[i][2] = min(dp[i - 1][0] + street[i][2], dp[i - 1][1] + street[i][2])


print(min(dp[-1]))