from collections import deque

direction = ((1, 0), (-1, 0), (0, -1), (0, 1))
n, k = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
s, answer_x, answer_y = map(int, input().split())

queue = deque()
for i in range(n):
    for j in range(n):
        if board[i][j]:
            queue.append([board[i][j], 0, i, j])
queue = sorted(queue,key=lambda x:x[0])
queue = deque(queue)

while queue:
    num, sec, y, x = queue.popleft()
    if sec >= s:
        break

    for dy, dx in direction:
        ny = dy + y
        nx = dx + x
        if 0 <= ny < n and 0 <= nx < n and not board[ny][nx]:
            board[ny][nx] = num
            queue.append([num, sec + 1, ny, nx])
print(board[answer_x - 1][answer_y - 1])
