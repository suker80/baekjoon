n, m, k = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

direction = ((1, 0), (0, 1), (-1, 0), (0, -1))


def rotate(i):
    dir = 0
    y, x = i, i
    dy, dx = direction[dir]
    cur = board[y][x]
    while dir < 4:
        dy, dx = direction[dir]
        ny, nx = y + dy, x + dx
        if 0 + i <= ny < n - i and 0 + i <= nx < m - i:
            next = board[ny][nx]
            board[ny][nx] = cur
            y = ny
            x = nx
            cur = next
        else:
            dir += 1


for _ in range(k):
    for i in range(min(n, m) // 2):
        rotate(i)
for i in range(n):
    print(*board[i])
