from collections import deque

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

visit = [[False] * m for _ in range(n)]

direction = [[1, 0], [-1, 0], [0, -1], [0, 1]]


def bfs(i, j):
    queue = deque()
    queue.appendleft([i, j])
    current = 0
    while queue:
        i, j = queue.popleft()
        current += 1
        visit[i][j] = True
        for dy, dx in direction:
            ny = i + dy
            nx = j + dx
            if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] == 1 and not visit[ny][nx]:
                queue.appendleft([ny, nx])
                visit[ny][nx] = True
    return current


answer = 0
count = 0
for i in range(n):
    for j in range(m):
        if not visit[i][j] and graph[i][j]:
            temp = bfs(i, j)
            count +=1
            answer = max(answer, temp)
print(count)
print(answer)