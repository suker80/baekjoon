import sys

n, m = map(int, input().split())

board = ['.' + input() + '.' for _ in range(n)]
board.insert(0, '.' * (m + 2))
board.append('.' * (m + 2))
direction = ((1, 0), (-1, 0), (0, -1), (0, 1))
coins = []
answer = 20
for i in range(n + 2):
    for j in range(m + 2):
        if board[i][j] == 'o':
            coins.append([i, j])


def check_drop(coin):
    if (coin[0] > n or coin[0] < 1) or (coin[1] > m or coin[1] < 1):
        return True
    else:
        return False


def solve(coins, count):
    global answer
    if count > 10:
        return
    if check_drop(coins[0]) != check_drop(coins[1]):
        answer = min(answer, count)
        return
    if check_drop(coins[0]) and check_drop(coins[1]):
        return
    for dy, dx in direction:
        next_coin = []
        for coin in coins:
            ny, nx = coin[0] + dy, coin[1] + dx
            if board[ny][nx] == '#':
                next_coin.append([coin[0], coin[1]])
            else:
                next_coin.append([ny, nx])
        solve(next_coin, count + 1)


solve(coins, 0)
print(answer) if answer <= 10 else print(-1)
