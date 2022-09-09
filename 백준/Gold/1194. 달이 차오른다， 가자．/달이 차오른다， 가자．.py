n,m= map(int,input().split())
import sys
input = sys.stdin.readline
from collections import deque
graph = [list(map(str,input().rstrip())) for _ in range(n)]

direction = [[1,0],[-1,0],[0,-1],[0,1]]
visit = [[[0] * m for _ in range(n)] for _ in range(0b111111+1)]

# visit = [bit,height,width]

answer= 0
a_bit= 97
queue = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == '0':
            queue.append([i,j,0,0b000000])
            graph[i][j] = '.'

while queue:
    y,x,count,bit= queue.popleft()

    visit[bit][y][x] = 1

    for dy,dx in direction:
        ny,nx = dy+y,dx+x

        if 0<=ny<n and 0<=nx<m and visit[bit][ny][nx] == False and graph[ny][nx] != '#':

            if 65<=ord(graph[ny][nx])<=70:
                if 1<<(ord(graph[ny][nx].lower()) - 97) & bit:
                    queue.append([ny,nx,count+1,bit])
                    visit[bit][ny][nx] = 1
                continue
            elif 97<=ord(graph[ny][nx]) <= 102 :
                next_bit = bit |(1<<ord(graph[ny][nx]) - 97)
                queue.append([ny,nx,count+1,next_bit])
                visit[bit][ny][nx] = 1
            elif graph[ny][nx] == '.':
                queue.append([ny, nx, count + 1, bit])
                visit[bit][ny][nx] = 1
            elif graph[ny][nx] == '1':
                print(count+1)
                sys.exit()



print(-1)





