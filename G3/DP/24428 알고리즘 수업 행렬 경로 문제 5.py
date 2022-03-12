m = int(input())

graph = [list(map(int, input().split())) for _ in range(m)]

k = int(input())
visit = [[False] * m for _ in range(m)]
for i in range(k):
    r, c = map(int, input().split())
    visit[r - 1][c - 1] = True

dp = [[[0] * m for _ in range(m)] for _ in range(4)]

if visit[0][0]:
    dp[1][0][0] = graph[0][0]
else:
    dp[0][0][0] = graph[0][0]

for count in range(3):
    for i in range(m):
        for j in range(m):
            if not dp[count][i][j]:
                continue
            if i < m - 1:
                if visit[i + 1][j]:
                    dp[count + 1][i + 1][j] = max(dp[count + 1][i + 1][j],
                                                  dp[count][i][j] + graph[i + 1][j])
                else:
                    dp[count][i + 1][j] = max(dp[count][i + 1][j], dp[count][i][j] + graph[i + 1][j])
            if j < m - 1:
                if visit[i][j + 1]:
                    dp[count + 1][i][j + 1] = max(dp[count + 1][i][j + 1],
                                                  dp[count][i][j] + graph[i][j + 1])
                else:
                    dp[count][i][j + 1] = max(dp[count][i][j + 1], dp[count][i][j] + graph[i][j + 1])

for i in range(m):
    for j in range(m):
        if not dp[3][i][j]: continue
        if i < m - 1:
            dp[3][i + 1][j] = max(dp[3][i + 1][j], dp[3][i][j] + graph[i + 1][j])
        if j < m - 1:
            dp[3][i][j + 1] = max(dp[3][i][j + 1], dp[3][i][j] + graph[i][j + 1])

print(dp[3][m - 1][m - 1]) if dp[2][m - 1][m - 1] else print(-1)
