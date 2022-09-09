n = int(input())
m= int(input())

import sys

input = sys.stdin.readline

INF = float('inf')
graph = [[INF] * (n) for _ in range(n)]
trace = [[-1]* n for _ in range(n)]

for i in range(m):
    a,b,c = map(int,input().split())

    if graph[a-1][b-1] > c:
        graph[a-1][b-1] = c
for k in range(n):
    graph[k][k] = 0
    for i in range(n):
        for j in range(n):

            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                trace[i][j] = k

def find_path(i,j):
    if trace[i][j] == -1:
        return []
    k = trace[i][j]

    return find_path(i,k) +[k+1] +find_path(k,j)

for i in range(n):
    for j in range(n):
        print(0,end=' ') if graph[i][j] == INF else print(graph[i][j],end=' ')
    print('')

for i in range(n):
    for j in range(n):
        if graph[i][j] in [0,INF]:
            print(0)
            continue
        path = [i+1] +find_path(i,j) + [j+1]
        print(len(path), end = ' ')
        print(*path)