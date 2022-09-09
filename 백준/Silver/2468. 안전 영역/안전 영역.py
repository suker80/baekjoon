n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

max_val, min_val = max([max(i) for i in graph]), min([min(i) for i in graph])

safety_zone = 1

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

from collections import deque


def bfs(start, current, visited):
    queue = deque([start])



    while queue:
        y, x = queue.popleft()
        visited[y][x] = 1
        for dy, dx in direction:

            ny, nx = y + dy, x + dx

            if 0 <= ny < n and 0 <= nx < n and visited[ny][nx] == 0 and graph[ny][nx] > current:
                queue.append((ny, nx))
                visited[ny][nx] = 1
    return visited


for current in range(min_val, max_val):
    visited = [[0] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > current and visited[i][j] == 0:
                visited = bfs((i, j), current, visited)
                count += 1
    safety_zone = max(safety_zone, count)

print(safety_zone)