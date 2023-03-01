import sys
from itertools import *


def check_dir(user, arduino):
    if user[0] > arduino[0]:
        dy = 1
    elif user[0] == arduino[0]:
        dy = 0
    else:
        dy = -1

    if user[1] > arduino[1]:
        dx = 1
    elif user[1] == arduino[1]:
        dx = 0
    else:
        dx = -1
    return dy, dx


direction = ((0, 0), (1, -1), (1, 0), (1, 1), (0, -1), (0, 0), (0, 1), (-1, -1), (-1, 0), (-1, 1))
n, m = map(int, input().split())

board = [list(input()) for _ in range(n)]

command = input()
arduinoes = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 'I':
            user = [i, j]
        elif board[i][j] == 'R':
            arduinoes.append([i, j])

for i, c in enumerate(command):
    c = int(c)
    dy, dx = direction[c]
    y = user[0]
    x = user[1]
    board[y][x] = '.'
    ny, nx = y + dy, x + dx
    if board[ny][nx] == 'R':
        print('kraj', i + 1)
        sys.exit()

    board[ny][nx] = 'I'
    user = [ny, nx]
    next_arduino = []
    for arduino in arduinoes:
        y, x = arduino
        board[y][x] = '.'

    for arduino in arduinoes:
        y, x = arduino
        dy, dx = check_dir(user, arduino)
        ny, nx = dy + y, dx + x
        if board[ny][nx] == 'I':
            print('kraj', i + 1)
            sys.exit()
        elif board[ny][nx] == '.':
            next_arduino.append([ny, nx])
            board[ny][nx] = 'R'
        elif board[ny][nx] == 'R':
            board[ny][nx] = 'B'

    arduinoes.clear()
    for arduino in next_arduino:
        y, x = arduino
        if board[y][x] == 'B':
            board[y][x] = '.'
            continue
        arduinoes.append(arduino)

for i in range(n):
    print(''.join(board[i]).replace('B', '.'))
