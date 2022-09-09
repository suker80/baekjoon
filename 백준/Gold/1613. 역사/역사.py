import sys
n,m = map(int,input().split())

input = sys.stdin.readline
graph= [[0]*n for _ in range(n)]

for i in range(m):
    a,b = map(int,input().split())
    graph[a-1][b-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] and graph[k][j] :
                graph[i][j] = 1

q = int(input())

for i in range(q):

    a,b = map(int,input().split())

    if graph[a-1][b-1]:
        print(-1)
    elif graph[b-1][a-1]:
        print(1)
    else:
        print(0)