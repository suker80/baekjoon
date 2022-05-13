from collections import defaultdict, deque
from heapq import *

direction = [(1, 0), (0, 1)]
INF = 123456789

n, m = map(int, input().split())
k = int(input())
graph = [[0] * m for _ in range(n)]
for _ in range(k):
    a, b, c = map(int, input().split())
    graph[a - 1][b - 1] = c
left, right = 0, (n + m)

while left < right:
    dp = [[-1] * m for _ in range(n)]
    mid = (left + right) // 2
    dp[0][0] = mid
    for i in range(n):
        for j in range(m):

            if i and dp[i - 1][j] >= 0:
                dp[i][j] = max(dp[i - 1][j] - 1 + graph[i - 1][j], dp[i][j])
            if j and dp[i][j - 1] >= 0:
                dp[i][j] = max(dp[i][j - 1] - 1 + graph[i][j - 1], dp[i][j])

    if dp[-1][-1] >= 0:
        right = mid
    else:
        left = mid + 1

print(left)
