n, m = map(int, input().split())

from collections import deque
from heapq import heappop, heappush

board = [list(map(str, input())) for _ in range(n)]

visit = [[0] * n for _ in range(n)]

direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def bfs(start):
    start += [0]

    temp_visit = [[0] * n for _ in range(n)]

    queue = deque([start])

    while queue:
        y, x, dist = queue.popleft()

        if board[y][x] == 'K' and visit[y][x] == 0:
            heappush(heap,[dist,y,x,])
        temp_visit[y][x] = 1

        for dy, dx in direction:
            ny, nx = dy + y, dx + x

            if 0 <= ny < n and 0 <= nx < n and board[ny][nx] != '1' and temp_visit[ny][nx] == 0:
                queue.append([ny, nx,dist+1])
                temp_visit[ny][nx] = 1


heap = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 'S':
            visit[i][j] = 1
            start = [i, j]


bfs(start)

find_key = 0 

answer = 0
while heap:
    d,y,x = heappop(heap)

    if not visit[y][x]:
        answer += d
        visit[y][x] = 1
        bfs([y,x])
        find_key += 1


print(answer) if find_key == m else print(-1)