n = int(input())
import copy
import sys
graph = [list(map(int,input().split())) for _ in range(n)]
temp_graph = copy.deepcopy(graph)


for k in range(n):
    for i in range(n):
        for j in range(n):
            if i==k or j==k : continue
            if graph[i][j] > graph[i][k] + graph[k][j] :
                print(-1)
                sys.exit()
            if graph[i][j] == graph[i][k] + graph[k][j]:
                temp_graph[i][j] = 0

print(sum([sum(t) for t in temp_graph]) //2)


