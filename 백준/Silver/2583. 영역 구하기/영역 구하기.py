m, n, k = map(int, input().split())

rect = [list(map(int, input().split())) for i in range(k)]

graph = [[0] * n for _ in range(m)]

visited = [[0] * n for _ in range(m)]
from collections import deque
for x1, y1, x2, y2 in rect:

    for i in range(m - y2, m - y1):
        for j in range(x1, x2):
            graph[i][j] = 1
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def dfs(start, visited):
    queue = deque([start])
    count = 1
    while queue:

        y, x = queue.popleft()
        visited[y][x]= 1
        for dy, dx in direction:
            ny, nx = y + dy, x + dx

            if 0 <= ny <= m - 1 and 0 <= nx <= n - 1 and visited[ny][nx] ==0 and graph[ny][nx] == 0:
                visited[ny][nx] = 1
                count += 1

                queue.append((ny, nx))

    return count, visited


graph = [[0] * n for _ in range(m)]

visited = [[0] * n for _ in range(m)]
for x1, y1, x2, y2 in rect:

    for i in range(m - y2, m - y1):
        for j in range(x1, x2):
            graph[i][j] = 1
queue = deque()
output = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0 and visited[i][j] == 0:
            count, visited = dfs((i, j), visited)
            output.append(count)
output.sort()
print(len(output))
print(*output)