n, m = map(int, input().split())

import sys

sys.setrecursionlimit(300000)
graph = [list(map(str, input())) for _ in range(n)]

direction = {'D': [1, 0], 'U': [-1, 0], 'L': [0, -1], 'R': [0, 1]}

case = [[-1] * m for _ in range(n)]

visit = [[0] * m for _ in range(n)]

def dfs(y,x):

    if case[y][x] != -1 :
        return case[y][x]

    dy,dx = direction[graph[y][x]]
    ny,nx = dy+y,dx+x
    visit[y][x] = 1
    if 0<=ny<n and 0<=nx<m:

        if visit[ny][nx] == 1 and case[ny][nx] == -1:
            return 0

        can = dfs(ny,nx)

        case[y][x] = can


    else:
        case[y][x] = 1

    return case[y][x]
answer = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j):
            answer += 1
print(answer)