from collections import deque
from heapq import *

direction = ((1, 0), (-1, 0), (0, 1), (0, -1))


def manhattan(a, b):
    return sum(abs(val1 - val2) for val1, val2 in zip(a, b))


n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
dist = [[float('inf')] * m for _ in range(n)]

trees = []
for i in range(n):
    for j in range(m):
        if board[i][j] == '+':
            trees.append([i, j])
            dist[i][j] = 0
        elif board[i][j] == 'V':
            start = [i, j]
        elif board[i][j] == 'J':
            end = [i, j]

queue = deque()
for tree in trees:
    queue.append([tree[0], tree[1], 0])
while queue:
    y, x, cnt = queue.popleft()
    dist[y][x] = cnt
    for dy, dx in direction:
        ny, nx = y + dy, x + dx
        if 0 <= ny < n and 0 <= nx < m and dist[ny][nx] > cnt + 1:
            dist[ny][nx] = cnt + 1
            queue.append([ny, nx, cnt + 1])


def dijkstra():
    answer_dist = [[-float('inf')] * m for _ in range(n)]
    heap = []
    heap.append([-dist[start[0]][start[1]], start[0], start[1]])
    while heap:
        cur_min, y, x = heappop(heap)

        if [y,x] == end:
            return answer_dist[end[0]][end[1]]


        for dy, dx, in direction:
            ny, nx = dy + y, dx + x
            if 0 <= ny < n and 0 <= nx < m:
                next_dist = min(-cur_min, dist[ny][nx])

                if next_dist > answer_dist[ny][nx]:
                    answer_dist[ny][nx] = next_dist
                    heappush(heap, [-next_dist, ny, nx])


print(dijkstra())
