import sys
from collections import deque


def solution(board):
    direction = ((1, 0), (0, 1), (-1, 0), (0, -1))
    n = len(board)
    m = len(board[0])
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                start_y, start_x = i, j

    queue = deque()
    queue.append([0, start_y, start_x])
    answer = float('inf')
    visit = [[False] * m for _ in range(n)]

    while queue:
        count, y, x = queue.popleft()
        visit[y][x] = True
        if board[y][x] == 'G':
            return count

        for dy, dx in direction:
            ny, nx = y, x
            while 0 <= ny + dy < n and 0 <= nx + dx < m and board[ny + dy][nx + dx] != 'D':
                ny += dy
                nx += dx
            if not visit[ny][nx]:
                visit[ny][nx] = True
                queue.append([count + 1, ny, nx])
    return -1

