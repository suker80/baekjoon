n, k, r = map(int, input().split())

graph = [[0] * n for _ in range(n)]

from collections import deque

direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
road = [[[[0] * n for _ in range(n)] for _ in range(n)] for _ in range(n)]
for i in range(1, r + 1):
    a, b, c, d = map(int, input().split())

    road[a - 1][b - 1][c - 1][d - 1] = 1
    road[c - 1][d - 1][a - 1][b - 1] = 1

cow_graph = [[0] * n for _ in range(n)]
for i in range(k):
    a, b = map(int, input().split())
    cow_graph[a - 1][b - 1] = 1


def bfs(y, x):
    queue = deque([[y, x]])

    visit = [[False] * n for _ in range(n)]
    visit[y][x] = 1
    count = 1
    while queue:

        y, x = queue.popleft()
        visit[y][x] = 1
        for dy, dx in direction:
            ny, nx = dy + y, dx + x

            if 0 <= ny < n and 0 <= nx < n and visit[ny][nx] == 0:

                if road[y][x][ny][nx] == 1: continue

                visit[ny][nx] = 1
                queue.append([ny, nx])
                if cow_graph[ny][nx] == 1:
                    count += 1
    return k - count


answer = 0
for i in range(n):
    for j in range(n):
        if cow_graph[i][j] == 1:
            answer += bfs(i, j)
print(answer // 2)
