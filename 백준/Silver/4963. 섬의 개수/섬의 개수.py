from collections import deque

import sys
input = sys.stdin.readline

direciton = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, -1], [-1, 1]]
def bfs(y, x):
    global answer
    visit[y][x] = 1
    queue = deque([[y, x]])
    while queue:
        y, x = queue.popleft()
        for dy, dx in direciton:
            ny, nx = dy + y, x + dx

            if 0 <= ny < h and 0 <= nx < w and visit[ny][nx] == 0 and graph[ny][nx]:
                queue.append([ny, nx])
                visit[ny][nx] = 1
while True:
    w,h = map(int,input().split())
    if w == 0 and h== 0 :
        break
    graph = [list(map(int,input().split())) for _ in range(h)]
    visit = [[0] * w for _ in range(h)]



    count = 0
    for i in range(h):
        for j in range(w):
            if visit[i][j] == 0 and graph[i][j] :
                bfs(i, j)
                count += 1

    print(count)
