n, m, c = map(int, input().split())
mod = 1_000_007

board = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(c):
    a, b = map(int, input().split())
    board[a][b] = i + 1
# dp[i][j][k][l] = i,j일때 이전에 방문한 오락실이 k이고 l개 방문했을때의 개수


dp = [[[[0] * (c + 1) for _ in range(c + 1)] for _ in range(m + 2)] for _ in range(n + 2)]

if board[1][1]:
    dp[1][1][board[1][1]][1] = 1
else:
    dp[1][1][0][0] = 1
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if not board[i][j]:
            for k in range(c + 1):
                for l in range(c + 1):
                    dp[i][j][k][l] += (dp[i - 1][j][k][l] + dp[i][j - 1][k][l]) % mod
        else:
            for k in range(board[i][j]):
                for l in range(1, c + 1):
                    dp[i][j][board[i][j]][l] += (dp[i - 1][j][k][l-1] + dp[i][j - 1][k][l-1]) % mod

answer = [0] * (c+1)
for i in range(c+1):
    for j in range(c+1):
        answer[j] += dp[n][m][i][j]
        answer[j] %= mod
print(*answer)

