n, m = map(int, input().split())
import copy
from collections import deque
import sys
graph=[]
for i in range(n):
    graph.append([int(_) for _ in input()])
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

flag = True

start = (0, 0)
count_map = [[0] * m for _ in range(n)]

min_dist = float('inf')

graph = [graph,copy.deepcopy(graph)]
def bfs(start,graph):
    queue = deque([start])
    global min_dist
    while queue:

        flag,y,x = queue.popleft()

        for dy, dx in direction:
            ny, nx = dy + y, dx + x

            if 0 <= ny < n and 0 <= nx < m:

                if graph[1][ny][nx] == 1 and flag:
                    graph[0][ny][nx] = graph[1][y][x] +1
                    queue.append((False,ny,nx))


                if graph[flag][ny][nx] == 0:
                    queue.append((flag,ny, nx))
                    graph[flag][ny][nx] = graph[flag][y][x] +1

                    if ny == n - 1 and nx == m - 1:
                        return graph[flag][ny][nx]
    return -1


graph[0][0][0] = 1
graph[1][0][0] = 1

print(1) if n==1 and m== 1 else print(bfs((flag,0,0),graph))