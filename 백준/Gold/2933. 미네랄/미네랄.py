r,c = map(int,input().split())
from collections import deque
mineral = [list(map(str,input())) for _ in range(r)]

n = int(input())
stick_size = list(map(int,input().split()))

direction = [(0,1),(0,-1),(1,0),(-1,0)]


def bfs(start):
    global visit
    touch_bottom = False
    queue =deque([start])
    y,x = start
    visit[y][x] = 1
    cluster = []
    cluster.append(start)
    while queue:
        y,x = queue.popleft()
        if y == r-1: touch_bottom = True
        for dy,dx in direction:
            ny,nx = dy+y ,dx+x
            if 0<=ny<r and 0<=nx<c and visit[ny][nx] == 0 and mineral[ny][nx] == 'x':
                queue.append([ny,nx])
                cluster.append([ny,nx])
                visit[ny][nx] = 1
    cluster.sort(reverse=True)
    if touch_bottom:
        return
    else:
        return cluster



def drop_cluster(cluster):

    bottom = []
    max_drop = float('inf')

    for clu in cluster:
        y,x = clu

        if mineral[y+1][x] == '.':
            bottom.append([y,x])

    for bot in bottom:
        depth = 0
        y,x= bot
        while y+1 < r and mineral[y+1][x] == '.':


            depth +=1
            y+=1
        if [y+1,x] not in cluster:
            max_drop = min(depth,max_drop)

    if max_drop != float('inf'):
        for clu in cluster:
            y,x = clu
            mineral[y][x] = '.'
        for clu in cluster:
            y,x = clu
            try:
                mineral[y+max_drop][x] = 'x'
                visit[y+max_drop][x] = 1
            except:
                raise ImportError

for i,stick in enumerate(stick_size):
    destroy= False
    if i %2 == 0:
        for j in range(c):
            if mineral[r-stick][j] == 'x':
                mineral[r-stick][j] = '.'
                destroy = True
                break
    else:
        for j in range(c-1,-1,-1):
            if mineral[r-stick][j] == 'x':
                mineral[r-stick][j] = '.'
                destroy= True
                break
    visit = [[0] * c for _ in range(r)]
    if destroy:
        for dy,dx in direction:
            ny,nx = r-stick + dy,j+dx
            if 0<=ny<r and 0<=nx<c and mineral[ny][nx] == 'x' and visit[ny][nx] == 0:
                cluster = bfs([ny,nx])
                if cluster:
                    drop_cluster(cluster)
                    break



for _ in mineral:
    print(''.join(_))

