board = [list(map(int, input().split())) for _ in range(9)]
from collections import deque
import sys
pos = deque()
cell_xy = [[(1,1),(1,4),(1,7)]
    ,[(4,1),(4,4),(4,7)]
    ,[(7,1),(7,4),(7,7)]
           ]
for i in range(9):
    for j in range(9):

        if board[i][j] == 0:
            pos.append((i, j))

count = 0
def check(count):
    #### 가로체크 #####


    if count == len(pos):

        for i in board:
            print(*i)
        sys.exit()
    else:
        y, x = pos[count]

        num_list = set(range(1, 10))
        num_list = num_list - set(board[y])

        for i in range(9):
            num_list.discard(board[i][x])
        cell_y,cell_x = cell_xy[y//3][x//3]

        for i in [-1,0,1]:
            for j in [-1,0,1]:
                num_list.discard(board[cell_y+i][cell_x+j])
        for num in num_list:
            board[y][x] =num
            check(count + 1)
            board[y][x] = 0
check(0)