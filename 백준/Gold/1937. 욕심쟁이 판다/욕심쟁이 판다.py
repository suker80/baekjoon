n= int(input())

graph = [list(map(int,input().split())) for _ in range(n)]

direction = [(1,0),(-1,0),(0,-1),(0,1)]

visit = [[False] * n for _ in range(n)]


def dfs(start,count=0):
    y,x= start
    visit[y][x] = 1

    for dy,dx in direction:
        ny,nx = dy+y,dx+x
        count = 1
        if 0<=ny<n and 0<=nx<n and graph[ny][nx]>graph[y][x]:
            if visit[ny][nx] == False:
                count += dfs([ny,nx],count+1)
                visit[y][x] = max(visit[y][x] , count)
            else:
                visit[y][x] = max(visit[y][x],visit[ny][nx]+1)
    return visit[y][x]
answer= 0 
for i in range(n):
    for j in range(n):
        if visit[i][j] == False:
            answer= max(dfs([i,j],0),answer)

print(answer)



