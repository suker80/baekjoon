n = int(input())

dp = [float('inf')] * (1234567)
dp[1] = 0
dp[2] = 1
dp[3] = 1

for i in range(4, n + 1):
    if i % 3 == 0:
        dp[i] = min(dp[i // 3] + 1, dp[i])
    if i % 2 == 0:
        dp[i] = min(dp[i // 2] + 1, dp[i])
    dp[i] = min(dp[i - 1] + 1, dp[i])

answer = [n]
while (n != 1):
    temp_answer = n

    if n % 3 == 0 and dp[temp_answer] > dp[n // 3]:
        temp_answer = n // 3
    if n % 2 == 0 and dp[temp_answer] > dp[n // 2]:
        temp_answer = n // 2

    if dp[temp_answer] > dp[n - 1]:
        temp_answer = n - 1
    n = temp_answer
    answer.append(n)
print(len(answer) - 1)
print(*answer)
