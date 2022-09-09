n, m = map(int, input().split())

INF = float('inf')
graph = [[INF] * (n + 1) for _ in range(n + 1)]
answer = [['-'] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c
    answer[a][b] = b
    answer[b][a] = a

dist = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            dist[i][j] = 0
        else:
            dist[i][j] = graph[i][j]

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                answer[i][j] = answer[i][k]

for i in range(1,n+1):
    print(*answer[i][1:])
