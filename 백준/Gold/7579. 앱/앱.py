N, M = map(int, input().split())
A = [0] + list(map(int, input().split()))  # byte
C = [0] + list(map(int, input().split()))  # cost
dp = [[0 for _ in range(sum(C) + 1)] for _ in range(N + 1)]
result = sum(C)  # 열의 최댓값

for i in range(1, N + 1):
    byte = A[i]
    cost = C[i]

    for j in range( sum(C) + 1):
        if j < cost:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(byte + dp[i - 1][j - cost], dp[i - 1][j])

        if dp[i][j] >= M:
            result = min(result, j)
if M != 0:
    print(result)
else:
    print(0)