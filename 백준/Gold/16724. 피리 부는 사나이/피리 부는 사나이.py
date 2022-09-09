n, m = map(int, input().split())

graph = [input() for _ in range(n)]

direction = {'D': [1, 0], 'U': [-1, 0],
             'L': [0, -1], 'R': [0, 1]}

visit = [[0] * m for _ in range(n)]

cnt = 0
safe = [[0] * m for _ in range(n)]


def dfs(i, j):
    global cnt
    dy, dx = direction[graph[i][j]]
    visit[i][j] = True
    ny, nx = i + dy, j + dx

    if 0 <= ny < n and 0 <= nx < m:

        if visit[ny][nx]:

            if safe[ny][nx]:
                safe[i][j] = safe[ny][nx]
                return safe[ny][nx]
            else:
                cnt += 1
                safe[i][j] = cnt
                return safe[i][j]
        else:
            safe[i][j] = dfs(ny, nx)
            return safe[i][j]
    else:
        cnt += 1
        safe[i][j] = cnt
        return safe[i][j]


for i in range(n):
    for j in range(m):
        if not visit[i][j]:

            dfs(i, j)

print(cnt)