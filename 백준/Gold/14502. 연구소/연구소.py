n,m = map(int,input().split())

from itertools import combinations
from copy import deepcopy
graph = [list(map(int, input().split())) for _ in range(n)]

default_graph = deepcopy(graph)

from collections import deque
queue = deque()
walls = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            queue.append((i,j))
        elif graph[i][j] == 0:
            walls.append((i,j))

comb = combinations(walls,3)
default_queue = deepcopy(queue)
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up down left right
safe = 0
for com in comb:
    queue = deepcopy(default_queue)
    graph = deepcopy(default_graph)

    for x,y in com:
        graph[x][y] =1

    while queue:
        x, y = queue.popleft()

        for dx, dy in direction:
            x_2, y_2 = x + dx, y + dy
            if 0 <= x_2 < n and 0 <= y_2< m and graph[x_2][y_2] == 0:
                graph[x_2][y_2] = 2
                queue.append((x_2, y_2))
    result = sum([graph[i][j] == 0 for i in range(n) for j in range(m)])
    safe = max(safe,result)

print(safe)