n = int(input())

direction = ((1, -1), (1, 0), (1, 1), (-1, 0), (-1, 1), (-1, -1), (0, -1), (0, 1))
board = [list(input()) for _ in range(n)]

must_mine = '$'
not_mine = '.'
while True:
    change_pos = []
    for i in range(n):
        for j in range(n):
            if ord('1') <= ord(board[i][j]) <= ord('9'):
                count = 0
                for dy, dx in direction:
                    ny = i + dy
                    nx = j + dx

                    if 0 <= ny < n and 0 <= nx < n and (board[ny][nx] == '#' or board[ny][nx] == '$'):
                        count += 1

                if count == int(board[i][j]):
                    for dy, dx in direction:
                        ny = i + dy
                        nx = j + dx

                        if 0 <= ny < n and 0 <= nx < n and (board[ny][nx] == '#'):
                            change_pos.append([ny, nx])
            elif board[i][j] == '#':
                for dy, dx in direction:
                    ny = i + dy
                    nx = j + dx
                    if 0 <= ny < n and 0<= nx < n and board[ny][nx] == '0':
                        board[i][j] = '.'
    for y, x in change_pos:
        board[y][x] = must_mine
    for i in range(n):
        for j in range(n):
            if ord('1') <= ord(board[i][j]) <= ord('9'):

                count = 0
                for dy, dx in direction:
                    ny = i + dy
                    nx = j + dx

                    if 0 <= ny < n and 0 <= nx < n and (board[ny][nx] == '$'):
                        count += 1

                if count == int(board[i][j]):
                    for dy, dx in direction:
                        ny = i + dy
                        nx = j + dx

                        if 0 <= ny < n and 0 <= nx < n and (board[ny][nx] == '#'):
                            board[ny][nx] = not_mine
    if not change_pos:
        break

answer = 0

for i in range(n):
    for j in range(n):
        if board[i][j] == '#' or board[i][j] == must_mine:
            answer += 1

print(answer)

#
# n = int(input())
# board = [list(input()) for _ in range(n)]
# direction = ((1, -1), (1, 0), (1, 1), (-1, 0), (-1, 1), (-1, -1), (0, -1), (0, 1))
# answer = 0
# for i in range(n):
#     for j in range(n):
#         if board[i][j] == '#':
#             for dy, dx in direction:
#                 ny = i + dy
#                 nx = j + dx
#                 if 0 <= ny < n and 0 <= nx < n and board[ny][nx] == '0':
#                     break
#             else:
#                 answer+=1
# print(answer)
#
