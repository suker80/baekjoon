n, m = map(int, input().split())
from collections import deque

light = [[False] * n for _ in range(n)]
graph = [[[] for _ in range(n)] for _ in range(n)]
direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
for i in range(m):
    x, y, a, b = map(int, input().split())

    graph[x - 1][y - 1].append([a - 1, b - 1])

answer = 1

queue = deque()
queue.append([0, 0])
light[0][0] = True
move = [[False] * n for _ in range(n)]
move[0][0] = True
visit = [[False] * n for _ in range(n)]
visit[0][0] = True
while queue:
    x, y = queue.popleft()

    for a,b in graph[x][y]:
        if not light[a][b]:
            light[a][b] = True
            if move[a][b] and not visit[a][b]:
                queue.append([a, b])
            answer += 1

    for dy, dx in direction:
        ny, nx = y + dy, x + dx

        if 0 <= ny < n and 0 <= nx < n:
            move[nx][ny] = True
            if move[nx][ny] and light[nx][ny] and not visit[nx][ny]:
                queue.append([nx, ny])
                visit[nx][ny] = True
print(answer)
