a, b, d, N = map(int, input().split())

mod = 1_000

dp = [0] * (N + 1)
dp[0] = 1
for i in range(N + 1):
    if i < a :
        dp[i] = 1
        continue

    if i < b:
        dp[i] = ( dp[i-1] + dp[i-a] ) % mod
    else:
        dp[i] = (dp[i-1] + dp[i-a] - dp[i-b] + 1000 ) % mod


answer = dp[-1]
if N >= d :
    answer  = (dp[-1] + 1000 - dp[N-d] ) % 1000
print(answer)