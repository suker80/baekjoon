from collections import deque

n = int(input())

graph = [list(map(int, input())) for _ in range(n)]

visited = [[1] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == visited[i][j]:
            visited[i][j] = 0

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up down left right


def bfs(graph, node):
    global visited
    queue = deque([node])
    count = 0
    visited[node[0]][node[1]] = 1
    while queue:
        x, y = queue.popleft()

        count += 1

        for i in range(4):
            x_2, y_2 = x + direction[i][0], y + direction[i][1]

            if 0 <= x_2 < n and 0 <= y_2 < n and visited[x_2][y_2] == 0:
                visited[x_2][y_2] = 1
                queue.append((x_2, y_2))
    return count


cplx = 0
result = []
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            count = bfs(graph, (i, j))
            cplx += 1
            result.append(count)


print(cplx)
result = sorted(result)

print(*result,sep='\n')

