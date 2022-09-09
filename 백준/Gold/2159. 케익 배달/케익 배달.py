n = int(input())

max_size = 100000
start_y, start_x = map(int, input().split())

pos = [list(map(int, input().split())) for _ in range(n)]
INF = float('inf')

dp = [[INF] * 5 for _ in range(n)]

direction = [[1, 0], [-1, 0], [0, 1], [0, -1], [0, 0]]
start_pos = [[start_y, start_x]] * 5

y, x = pos[0]
for i in range(5):
    dy, dx = direction[i]
    ny, nx = dy + y, dx + x

    if 0 <= ny < max_size and 0 <= nx < max_size:
        dp[0][i] = abs(ny - start_y) + abs(nx - start_x)

for idx in range(1, n):
    next_pos = pos[idx]

    current_pos = [[pos[idx - 1][0] + direction[i][0], pos[idx - 1][1] + direction[i][1]] for i in range(5)]
    y, x = next_pos

    for i in range(5):
        for j in range(5):
            dy, dx = direction[j]
            ny, nx = y + dy, x + dx
            dist = abs(ny - current_pos[i][0]) + abs(nx - current_pos[i][1])
            dp[idx][j] = min(dp[idx-1][i] + dist,dp[idx][j])
print(min(dp[-1]))
