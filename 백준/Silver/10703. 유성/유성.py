from collections import defaultdict

n, m = map(int, input().split())

board = [list(input()) for _ in range(n)]
direction = ((1, 0), (-1, 0), (0, 1), (0, -1))
star = []
star_bottom = defaultdict(int)
for i in range(n):
    for j in range(m):
        if board[i][j] == 'X':
            star.append((i, j))
            board[i][j] = '.'
            star_bottom[j] = max(star_bottom[j], i)
count = 0
while True:
    flag = True

    for k, v in star_bottom.items():
        if board[v + count + 1][k] == '#':
            flag = False
            break
    if not flag:
        for i, j in star:
            board[i + count][j] = 'X'
        break

    count += 1
for i in range(n):
    print(''.join(board[i]))
