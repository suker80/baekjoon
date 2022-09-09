from collections import deque
import sys

r, c = map(int, input().split())

forest = [list(input()) for _ in range(r)]
water_queue = deque()
for i in range(r):
    for j in range(c):
        if forest[i][j] == 'S':
            queue = deque([(i, j)])
        if forest[i][j] == '*':
            water_queue.append((i, j))

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(queue):
    if len(queue) == 0:
        print('KAKTUS')
        sys.exit()

    next_queue = deque()
    while queue:
        y, x = queue.popleft()

        for dy, dx in direction:
            ny, nx = dy + y, dx + x
            if 0 <= ny < r and 0 <= nx < c and forest[ny][nx] == '.':
                next_queue.append((ny, nx))

            elif 0 <= ny < r and 0 <= nx < c and forest[ny][nx] == 'D':
                print(time)
                sys.exit()
    return next_queue


def water_bfs(queue):
    next_queue = deque()
    while queue:
        y, x = queue.popleft()

        for dy, dx in direction:
            ny, nx = dy + y, dx + x
            if 0 <= ny < r and 0 <= nx < c and forest[ny][nx] == '.':
                next_queue.append((ny, nx))
                forest[ny][nx] = '*'
    return next_queue


time = 0

while True:
    time += 1
    queue = deque(set(queue) - set(water_queue))
    water_queue = water_bfs(water_queue)
    queue = bfs(queue)