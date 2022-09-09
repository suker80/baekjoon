t = int(input())
for _ in range(t):
    c = int(input())

    n= c+2

    graph = [list(map(int,input().split()))  for _ in range(n)]

    dist_graph= [[0]*(n) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i!=j:
                dist_graph[i][j] = 1 if abs(graph[i][0] - graph[j][0]) + abs(graph[i][1] - graph[j][1]) <=1000 else 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist_graph[i][k] and dist_graph[k][j] :
                    dist_graph[i][j]=1

    if dist_graph[0][-1] == 1:
        print('happy')
    else:
        print('sad')