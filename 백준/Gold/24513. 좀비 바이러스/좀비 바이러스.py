from collections import deque


def bfs(queue):
    next_queue = deque()

    while queue:
        y, x, virus = queue.popleft()
        visit[virus][y][x] = 1

        if board[y][x] == 3:
            continue

        for dy, dx in direction:
            ny = y + dy
            nx = x + dx

            if 0 <= ny < n and 0 <= nx < m and visit[virus][ny][nx] == 0:
                if board[ny][nx] == 0:
                    visit[virus][ny][nx] = 1
                    next_queue.append([ny, nx, virus])
    return next_queue


n, m = map(int, input().split())
direction = ((1, 0), (-1, 0), (0, 1), (0, -1))
board = [list(map(int, input().split())) for _ in range(n)]

visit = [[[0] * m for _ in range(n)] for _ in range(3)]

first_queue = deque()
second_queue = deque()
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            first_queue.append([i, j, 1])
        elif board[i][j] == 2:
            second_queue.append([i, j, 2])

while first_queue or second_queue:
    first_queue = bfs(first_queue)
    second_queue = bfs(second_queue)
    for y, x, _ in first_queue:
        if visit[1][y][x] and visit[2][y][x]:
            board[y][x] = 3
        else:
            board[y][x] = 1
    for y, x, _ in second_queue:
        if visit[1][y][x] and visit[2][y][x]:
            board[y][x] = 3
        else:
            board[y][x] =2

answer = [0, 0, 0]
for i in range(n):
    for j in range(m):
        if board[i][j] > 0:
            answer[board[i][j] - 1] += 1

print(*answer)
