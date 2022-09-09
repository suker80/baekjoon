from collections import defaultdict, deque
from heapq import *

direction = [(1, 0), (0, 1)]
INF = 123456789

n, m = map(int, input().split())
k = int(input())
oil = []
for _ in range(k):
    a, b, c = map(int, input().split())
    oil.append([a - 1, b - 1, c])
left, right = 0, (n + m - 2)
oil.sort(key=lambda x: (x[0], x[1]))
while left < right:
    mid = (left + right) // 2
    dp = [mid - a - b for a, b, c in oil]
    flag = False
    for i in range(k):
        if dp[i] <0:
            continue
        for j in range(k):
            oilA = oil[i]
            oilB = oil[j]
            if i == j: continue

            if oilA[0] <= oilB[0] and oilA[1] <= oilB[1]:

                dp[j] = max(dp[i] - ((oilB[0] - oilA[0]) + (oilB[1] - oilA[1])) + oilA[2],dp[j])

    for i in range(k):
        if dp[i] < 0:
            continue
        oil_y, oil_x, _ = oil[i]
        if dp[i] - ((n - oil_y - 1) + (m - oil_x - 1)) + _ >= 0:
            flag = True
    if flag:
        right = mid
    else:
        left = mid + 1
print(left)
