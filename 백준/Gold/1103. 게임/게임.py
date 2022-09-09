n, m = map(int, input().split())

graph = [[0] * m for _ in range(n)]

import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline

for i in range(n):
    for j, v in enumerate(list(map(str, input().rstrip()))):
        if ord('1') <= ord(v) <= ord('9'):
            graph[i][j] = int(v)
        else:
            graph[i][j] = 'H'

direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]

dp = [[0] * m for _ in range(n)]

visit = [[0] * m for _ in range(n)]


def dfs(i, j):
    if dp[i][j]:
        return dp[i][j]

    if visit[i][j] == 1:
        print(-1)
        sys.exit()
    visit[i][j] = 1
    m_val = 1
    for d, dir in enumerate(direction):

        dy, dx = dir
        ny, nx = i + (dy * graph[i][j]), j + (dx * graph[i][j])

        if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] != 'H' and [ny, nx] != [i, j]:
            m_val = max(dfs(ny, nx) + 1, m_val)
    dp[i][j] = m_val

    return dp[i][j]


print(dfs(0, 0))
