n= int(input())

graph = [list(map(int,input().split())) for _ in range(n)]
from collections import deque
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            shark = [i,j]
            graph[i][j] = 0
direction = [(0,1),(0,-1),(1,0),(-1,0)]
import sys
def search(shark):
    visit = [[0]* n for _ in range(n)]

    queue = deque([shark+[0]])
    y,x= shark
    visit[y][x] = 1
    fish = []
    fish_dist =10000
    while queue:
        y,x,dist = queue.popleft()
        if dist == fish_dist: break

        for dy,dx in direction:
            ny,nx = dy+y,dx+x
            if 0<=ny< n and 0<=nx <n and visit[ny][nx] == 0:

                if graph[ny][nx] >= 1 and graph[ny][nx] < size:
                    fish_dist = dist+1
                    fish.append([ny,nx,fish_dist])
                if graph[ny][nx] <=size:
                    queue.append([ny,nx,dist+1])
                visit[ny][nx] = 1
    fish.sort()
    if fish:
        return fish[0]
    else:
        print(sec)
        sys.exit(0)
size = 2
sec= 0
eat_fish = 0
while True:

    ny,nx,dist = search(shark)
    graph[ny][nx] = 0
    eat_fish += 1
    sec += dist
    shark = [ny,nx]

    if eat_fish == size:
        eat_fish = 0
        size +=1






