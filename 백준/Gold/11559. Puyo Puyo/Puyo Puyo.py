from collections import deque

n, m = 12, 6
board = [list(input()) for _ in range(n)]
direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
answer = 0


def find_blocks(i, j):
    queue = deque([[i, j]])
    travel = []
    while queue:
        y, x = queue.popleft()
        for dy, dx in direction:
            ny, nx = y + dy, dx + x
            if 0 <= ny < n and 0 <= nx < m and board[y][x] == board[ny][nx] and not visit[ny][nx]:
                visit[ny][nx] = True
                queue.append([ny, nx])
                travel.append([ny, nx])
    if len(travel) >= 4:
        return travel


def delete_blocks(t):
    for travel in t:
        for y, x in travel:
            board[y][x] = '.'


def move_blocks():
    for i in range(n - 1, -1, -1):
        for j in range(m):
            if board[i][j] == '.':
                for k in range(i - 1, -1, -1):
                    if board[k][j] != '.':
                        board[i][j] = board[k][j]
                        board[k][j] = '.'
                        break


while True:
    t = []

    visit = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] != '.':
                travel = find_blocks(i, j)
                if travel:
                    t.append(travel)
    if not t:
        print(answer)
        break
    if t:
        delete_blocks(t)
        move_blocks()
        answer += 1
