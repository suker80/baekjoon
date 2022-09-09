n, m = map(int, input().split())
k = int(input())

dp = [[0] * (n + 1) for _ in range(m + 1)]

roads = []
dp[0][0] = 1
for i in range(k):
    roads.append(list(map(int, input().split())))


def check(current, a, b, c, d):
    if current == [a, b, c, d] or current == [c, d, a, b]:
        return True
    else:
        return False


for i in range(m + 1):
    for j in range(n + 1):
        if j > 0:
            for a, b, c, d in roads:

                if check([j - 1, i, j, i], a, b, c, d):
                    break
            else:
                dp[i][j] += dp[i][j - 1]
        if i > 0:
            for a, b, c, d in roads:
                if check([j, i - 1, j, i], a, b, c, d):
                    break
            else:
                dp[i][j] += dp[i - 1][j]

print(dp[m][n])
