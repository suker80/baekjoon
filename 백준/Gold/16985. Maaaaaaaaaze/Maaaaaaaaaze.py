import sys
from itertools import permutations, combinations
from collections import deque

board = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]

answer = float('inf')

direction = [[0, 0, 1], [0, 0, -1], [0, 1, 0], [0, -1, 0], [1, 0, 0], [-1, 0, 0]]  ## z,y,x


def rotate(idx):
    return list(zip(*temp_board[idx][::-1]))


def bfs(z, y, x):
    if temp_board[z][y][x] == 0:
        return float('inf')
    visit = [[[0] * 5 for _ in range(5)] for _ in range(5)]
    visit[z][y][x] = 1
    queue = deque([[z, y, x]])
    while queue:
        z, y, x = queue.popleft()
        if z == 4 and y == 4 and x == 4:
            return visit[4][4][4] - 1
        for dz, dy, dx in direction:
            nz, ny, nx = dz + z, dy + y, dx + x

            if 0 <= nz < 5 and 0 <= ny < 5 and 0 <= nx < 5 and visit[nz][ny][nx] == 0 and temp_board[nz][ny][nx] == 1:
                queue.append([nz, ny, nx])
                visit[nz][ny][nx] = visit[z][y][x] + 1
    return float('inf')


for p in permutations(range(5), 5):
    temp_board = []
    for idx in p:
        temp_board.append(board[idx])
    for _ in range(4):
        for _ in range(4):
            for _ in range(4):
                for _ in range(4):
                    for _ in range(4):
                        count = bfs(0,0,0)
                        if count < answer:
                            answer = count
                        temp_board[4] = rotate(4)
                    temp_board[3] = rotate(3)
                temp_board[2] = rotate(2)
            temp_board[1] = rotate(1)
        temp_board[0] = rotate(0)

if answer == float('inf'):
    answer = -1
print(answer)