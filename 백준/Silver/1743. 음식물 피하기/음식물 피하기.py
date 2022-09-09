n, m, k = map(int, input().split())

graph = [[]]
visit = [[]]
for i in range(n):
    graph.append([0] * (m + 1))
    visit.append([0] * (m + 1))
for i in range(k):
    i, j = map(int, input().split())
    graph[i][j] = 1


def dfs(start, visit):
    queue = deque([start])
    count = 1
    while queue:
        x, y = queue.popleft()
        visit[x][y] = 1

        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 < nx <= n and 0 < ny <= m and visit[nx][ny] == 0 and graph[nx][ny] == 1:
                queue.append((nx, ny))
                visit[nx][ny] = 1
                count += 1
    return count, visit


direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up down left right
from collections import deque

queue = deque()
output = []
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if graph[i][j] == 1:
            count, visit = dfs((i, j), visit)
            output.append(count)
print(max(output))