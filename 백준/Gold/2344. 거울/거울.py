n, m = map(int, input().split())

direction = ((1, 0), (-1, 0), (0, 1), (0, -1))
mirror_direction = {1: 4, 2: 3, 3: 2, 4: 1}
board = []
board.append([0] + list(range(n + n + m + m, n + n + m, -1)) + [0])
for i in range(n):
    board.append([i + 1] + list(map(int, input().split())) + [n + m + n - i])
board.append([0] + list(range(n + 1, n + m + 1)) + [0])

answer = [0] * (n + n + m + m)
yx_pos = []
for i in range(n):
    yx_pos.append([i + 1, 1, 0, 1])
for i in range(m):
    yx_pos.append([n, i + 1, -1, 0])
for i in range(n):
    yx_pos.append([n - i,  m, 0, -1])
for i in range(m):
    yx_pos.append([1, m - i, 1, 0])

for i in range(n + n + m + m):
    y, x, dy, dx = yx_pos[i]
    while True:
        if y == 0 or y == n+1 or x == m+1 or x == 0:
            answer[i] = board[y][x]
            break
        if board[y][x] == 1:
            dy, dx = -dx, -dy
        y += dy
        x += dx
print(*answer)