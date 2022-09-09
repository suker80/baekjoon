n, m = map(int, input().split())

graph = [input() for i in range(n)]

graph = list(map(list, graph))
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            graph[i][j] = 1
        else:
            graph[i][j] = 0

from collections import deque

direction = [(1, 0), (-1, 0), (0, -1), (0, 1)]


def bfs(start):
    visit = [[0] * m for _ in range(n)]
    queue = deque([start])
    visit[start[0]][start[1]] = 1
    while queue:
        y, x = queue.popleft()
        for dy, dx in direction:

            ny, nx = dy + y, dx + x

            if 0 <= ny < n and 0 <= nx < m and visit[ny][nx] == 0 and graph[ny][nx] == 1:
                queue.append((ny, nx))
                visit[ny][nx] = visit[y][x] + 1

    return max([max(v) for v in visit])


dist = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            count = bfs((i, j))
            dist = max(dist, count)

print(dist - 1)