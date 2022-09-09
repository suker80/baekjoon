n,m= map(int,input().split())


graph = [[float('inf')] * n for _ in range(n)]

for i in range(m):
    a,b = map(int,input().split())

    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1

for k in range(n):
    graph[k][k] = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
bacon = [sum(i) for i in graph]

print(bacon.index(min(bacon)) + 1)


