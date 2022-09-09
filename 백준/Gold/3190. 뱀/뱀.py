import sys
from collections import deque

n = int(input())

k = int(input())

board = [[0] * (n) for _ in range(n)]

for _ in range(k):
    y, x = map(int, input().split())

    board[y-1][x-1] = 1
l = int(input())

sec, change = [], []
for _ in range(l):
    s, c = input().split()

    sec.append(int(s))
    change.append(c)
time = 0

snake = deque([(0, 0)])
default_direction = 3
direction_int = [0, 1, 2, 3]
direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # 위 왼 아래 오른
cur_dir = default_direction
y, x = snake[-1]
while 0 <= y < n and 0 <= x < n:
    y, x = snake[-1]

    board[y][x] = time+2
    if sec:
        next_time = sec[0]
    if time == next_time:
        sec.pop(0)
        change_direction = change.pop(0)
        if change_direction == 'D':
            cur_dir = cur_dir - 1 if cur_dir >= 1 else 3
        elif change_direction == 'L':
            cur_dir = cur_dir + 1 if cur_dir <= 2 else 0

    y,x = direction[cur_dir][0] + y, direction[cur_dir][1] + x
    time += 1


    if (y,x) in snake:
        break
    snake.append((y, x))
    ############### check apple ##########

    if 0 <= y < n and 0 <= x < n and board[y][x] == 1:
        board[y][x] = 0
    else:
        snake.popleft()

print(time)
