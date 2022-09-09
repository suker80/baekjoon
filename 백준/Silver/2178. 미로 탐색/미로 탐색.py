n , m = map(int,input().split())
graph= [[]]

for _ in range(n):
    graph.append([0] +[int(_) for _  in input()])

visit = dist = [[0] * (m+1) for _ in range(n+1)]
start = [1,1]
dist[1][1]= 1 
from collections import deque
queue = deque([start])
xx = [0,0,-1,1] # 위 아래 왼 오른
yy= [-1,1,0,0] # 위 아래 왼 오른

while queue:
    x,y = queue.popleft()
    if x == n and y == m:
        break

    for i in range(4):
        x_temp , y_temp  = x + xx[i] , y+yy[i]
        
        if 0<x_temp <= n and 0<y_temp <= m and visit[x_temp][y_temp] == 0 and graph[x_temp][y_temp] !=0:
            dist[x_temp][y_temp] = dist[x][y] + 1
            queue.append([x_temp,y_temp])
print(dist[n][m])