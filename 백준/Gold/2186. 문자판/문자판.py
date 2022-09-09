n, m, k = map(int, input().split())
from collections import deque

graph = [list(map(str, input())) for _ in range(n)]

word = input()

direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
start_pos = []

word_len = len(word)
dp = [[[-1] * m for _ in range(n)] for _ in range(word_len)]


def dfs(y, x, l):
    if l > word_len - 1: return 0

    if graph[y][x] != word[l]: return 0

    if graph[y][x] == word[-1] and l == word_len - 1:
        dp[l][y][x] = 1
        return dp[l][y][x]
    if dp[l][y][x] != -1:
        return dp[l][y][x]
    dp[l][y][x] = 0
    for dy, dx in direction:
        for jump in range(1,k+1):
            ny, nx = dy * jump + y, dx * jump + x
            if 0 <= ny < n and 0 <= nx < m:
                dp[l][y][x] += dfs(ny, nx, l + 1)

    return dp[l][y][x]


answer = 0
for i in range(n):
    for j in range(m):

        if graph[i][j] == word[0]:
            answer += dfs(i, j, 0)

print(answer)
