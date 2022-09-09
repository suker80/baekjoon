n = int(input())
from bisect import *

arr = [[_ + 1] + list(map(int, input().split())) for _ in range(n)]

arr.sort(key=lambda x: x[1], reverse=True)

dp = [0] * n

dp[0] = arr[0][2]

for i in range(1, n):
    height = arr[i][2]
    dp[i] = arr[i][2]
    for j in range(i):

        if arr[i][3] < arr[j][3] and arr[i][1] < arr[j][1]:
            dp[i] = max(dp[i], dp[j] + height)

answer_v = max(dp)

index = n - 1
answer = []
while index >= 0:
    if answer_v == dp[index]:
        answer.append(arr[index][0])
        answer_v -= arr[index][2]
    index -= 1
print(len(answer))
print(*answer, sep='\n')
