t = int(input())
for _ in range(t):
    m,n,k = map(int, input().split())

    graph = []
    visit = []
    for i in range(n):
        graph.append([0] * m)
        visit.append([0] * m)
    for i in range(k):
        j,i= map(int, input().split())
        graph[i][j] = 1

    def bfs(start, visit):
        queue = deque([start])
        while queue:
            y,x= queue.popleft()
            visit[y][x] = 1

            for dy, dx in direction:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny <n and visit[ny][nx] == 0 and graph[ny][nx] == 1:
                    queue.append((ny, nx))
                    visit[ny][nx] = 1
        return visit


    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up down left right
    from collections import deque

    output = 0
    for j in range(0, n):
        for i in range(0, m):
            if graph[j][i] == 1 and visit[j][i] == 0:
                visit[j][i] = 1
                visit = bfs((j,i), visit)
                output +=1
    print(output)