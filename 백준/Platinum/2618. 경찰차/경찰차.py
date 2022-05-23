n = int(input())
w = int(input())

car = [[[0, 0], [n - 1, n - 1]]]
for i in range(w):
    a, b = map(int, input().split())
    arr = [a - 1, b - 1]
    car.append([arr, arr])
dp = [[float('inf')] * (w + 1) for _ in range(w + 1)]
dp[0][0] = 0


def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


dp[1][0] = dist(car[1][0], car[0][0])
dp[0][1] = dist(car[0][1], car[1][1])
for i in range(w):
    for j in range(w):
        if i == j: continue

        if i > j:
            dp[i + 1][j] = min(dp[i][j] + dist(car[i + 1][0], car[i][0]), dp[i + 1][j])
            dp[i][i + 1] = min(dp[i][j] + dist(car[i + 1][1], car[j][1]), dp[i][i + 1])
        else:
            dp[i][j + 1] = min(dp[i][j] + dist(car[j + 1][1], car[j][1]), dp[i][j + 1])
            dp[j + 1][j] = min(dp[i][j] + dist(car[j + 1][0], car[i][0]), dp[j + 1][j])

answer = []

trace = float('inf')
trace_idx = []
for i in range(w):
    if trace > dp[i][w]:
        trace_idx = [i, w]
        trace = dp[i][w]
    if trace > dp[w][i]:
        trace_idx = [w, i]
        trace = dp[w][i]
print(trace)
while w:
    y, x = trace_idx

    flag = True
    if y == w:
        for i in range(y):
            if dp[i][x] + dist(car[i][0], car[y][0]) == trace and max(x, i) == w - 1:
                trace = dp[i][x]
                trace_idx = [i, x]
                answer.append(1)
                w -= 1
                break
        continue
    if x == w:
        for i in range(x):
            if dp[y][i] + dist(car[i][1], car[x][1]) == trace and max(i, y) == w - 1:
                trace = dp[y][i]
                trace_idx = [y, i]
                answer.append(2)
                w -= 1
                break
        continue

answer.reverse()
print('\n'.join(map(str, answer)))
