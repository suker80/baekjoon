import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

graph= [[0] *(n+1) for _ in range(n+1)]
for i in range(m):

    a,b=map(int,input().split())

    graph[a][b]= 1


for k in range(1,n+1):
    for i in range(1,n + 1):
        for j in range(1,n + 1):
            if graph[i][k] and graph[k][j]:
                graph[i][j] =1


for i in range(1,n+1):
    answer = 0

    for j in range(1,n+1):
        if i==j:continue

        if not graph[i][j] and not  graph[j][i] :
            answer += 1

    print(answer)

