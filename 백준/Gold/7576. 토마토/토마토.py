import sys
input = sys.stdin.readline
n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(m)]
if sum([graph[i][j] == 0 for i in range(m) for j in range(n)]):
    result = [[0] * n for _ in range(m)]
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up down left right

    from collections import deque


    def dfs(graph, node,result):
        queue = deque([node])

        visited[node[0]][node[1]] = 1
        while queue:
            x, y = queue.popleft()

            for dx, dy in direction:
                x_2, y_2 = x + dx, y + dy
                if 0 <= x_2 < m and 0 <= y_2 < n and visited[x_2][y_2] == 0 and graph[x_2][y_2] == 0:
                    if result[x_2][y_2] != 0:
                        result[x_2][y_2] = min(result[x][y] + 1, result[x_2][y_2])
                    else:
                        result[x_2][y_2] = result[x][y] + 1
                    visited[x_2][y_2] = 1
                    queue.append((x_2, y_2))
        return result

    queue = deque([])
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                queue.append([i,j])


    visited = [[0] * n for _ in range(m)]
    while queue:
        x, y = queue.popleft()
        visited[x][y] = 1
        for dx, dy in direction:
            x_2, y_2 = x + dx, y + dy
            if 0 <= x_2 < m and 0 <= y_2 < n and visited[x_2][y_2] == 0 and graph[x_2][y_2] == 0:

                result[x_2][y_2] = result[x][y] + 1
                visited[x_2][y_2] = 1
                queue.append((x_2, y_2))

    for i in range(m):
        for j in range(n):
            if result[i][j] == 0 and  graph[i][j] == 0:
                print(-1)
                sys.exit()
    print(max([max(res) for res in result]))
else:
    print(0)
