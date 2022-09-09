n, height = map(int, input().split())

arr = [int(input()) for _ in range(n)]

dp = [[0] * (1 << n) for _ in range(n)]

for i in range(n):
    dp[i][1 << i] = 1

for i in range(1,1 << n):
    for j in range(n):
        for k in range(n):

            if i & (1 << k) == 0 and abs(arr[j] - arr[k]) > height:
                dp[k][i | 1<<k] += dp[j][i]
answer = 0

for i in range(n):
    answer += dp[i][-1]
print(answer)
