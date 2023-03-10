from heapq import *

n, m, t, d = map(int, input().split())

board = [list(input()) for _ in range(n)]
direction = ((1, 0), (0, 1), (0, -1), (-1, 0))
for i in range(n):
    for j in range(m):
        if board[i][j].isupper():
            board[i][j] = ord(board[i][j]) - ord('A')
        else:
            board[i][j] = 26 + ord(board[i][j]) - ord('a')

time_board, back_time = [[float('inf')] * m for _ in range(n)], [[float('inf')] * m for _ in range(n)]
back_time[0][0] = 0
heap = []
heap.append([0, 0, 0])

while heap:
    cur_time, y, x = heappop(heap)
    if cur_time > d:
        break
    if cur_time > back_time[y][x]:
        continue

    for dy, dx in direction:
        ny, nx = dy + y, dx + x
        if 0 <= ny < n and 0 <= nx < m:
            diff = board[y][x] - board[ny][nx]

            if abs(diff) > t:
                continue
            if diff <= 0:
                spent_time = 1
            else:
                spent_time =  (diff ** 2)
            if spent_time + cur_time < back_time[ny][nx]:
                heappush(heap, [cur_time + spent_time, ny, nx])
                back_time[ny][nx] = cur_time+spent_time

high = 0
time_board[0][0] = 0
heap = []
heap.append([0, 0, 0])
while heap:
    cur_time, y, x = heappop(heap)
    if cur_time > d:
        break
    if cur_time > time_board[y][x]:
        continue

    for dy, dx in direction:
        ny, nx = dy + y, dx + x
        if 0 <= ny < n and 0 <= nx < m:
            diff = board[y][x] - board[ny][nx]

            if abs(diff) > t:
                continue
            if diff >= 0:
                spent_time = 1
            else:
                spent_time =  (diff ** 2)
            if spent_time+cur_time < time_board[ny][nx]:
                heappush(heap, [cur_time + spent_time, ny, nx])
                time_board[ny][nx] = cur_time+spent_time
answer = 0
for i in range(n):
    for j in range(m):
        if time_board[i][j] + back_time[i][j] <= d:
            answer = max(answer, board[i][j])
print(answer)