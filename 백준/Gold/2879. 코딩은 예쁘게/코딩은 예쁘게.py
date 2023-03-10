n = int(input())

arr = list(map(int, input().split()))
answer = list(map(int, input().split()))

dp = []

for i in range(n):
    dp.append(arr[i] - answer[i])

left = 0

answer = 0


def solve(left, right):
    global answer
    if left == right:
        answer += abs(dp[left])
        dp[left] = 0
        return
    min_value = float('inf')
    for i in range(left, right + 1):
        min_value = min(min_value, abs(dp[i]))
    if dp[left] < 0:
        for i in range(left, right + 1):
            dp[i] += min_value
    else:
        for i in range(left, right + 1):
            dp[i] -= min_value
    answer += min_value
    next_left = left
    for i in range(left + 1, right + 1):
        if dp[next_left] * dp[i] <= 0:
            solve(next_left, i - 1)
            next_left = i
    solve(next_left ,right)


for i in range(1, n):
    if dp[left] * dp[i] <= 0:
        solve(left, i - 1)
        left = i
    else:
        continue

solve(left, n - 1)
print(answer)
