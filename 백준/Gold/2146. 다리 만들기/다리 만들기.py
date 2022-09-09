import sys
input = sys.stdin.readline
n = int(input())
import copy

graph = [list(map(int,input().split())) for _ in range(n)]
from collections import deque

island =copy.deepcopy(graph)
direction = [(1,0),(-1,0),(0,1),(0,-1)]
pos = []
is_island = 1001
def bfs(start):

    queue = deque([start])

    while queue:

        y,x = queue.popleft()
        graph[y][x] = is_island
        for dy,dx in direction:
            ny,nx = dy+y,dx+x
            if 0<=ny<n and 0<=nx<n and graph[ny][nx] ==1 :
                queue.append((ny,nx))
                graph[ny][nx] = is_island
                pos.append([ny,nx,is_island])

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            bfs((i,j))
            pos.append([i, j, is_island])
            is_island += 1
def build_bridge(start):


    queue = deque(start)

    while queue:
        y,x,current = queue.popleft()

        for dy,dx in direction:
            ny,nx = dy+y,dx+x
            if 0 <= ny < n and 0 <= nx < n:
                if island[ny][nx] == 0:
                    queue.append([ny,nx,current])
                    island[ny][nx] = island[y][x] + 1
                    graph[ny][nx] = current
                elif graph[ny][nx] > 1000 and graph[ny][nx] != current:
                    print(island[y][x] -2 +island[ny][nx])
                    sys.exit()

build_bridge(pos)