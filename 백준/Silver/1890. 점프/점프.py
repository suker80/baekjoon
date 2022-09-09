n = int(input())

board = []
import sys
from collections import deque
for _ in range(n):
    board.append(list(map(int,input().split())))

dp = [[0]* n for _ in range(n)]
dp_idx = deque([(0,0)])
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        jump = board[i][j]
        if jump == 0:
            continue
        if i+jump <n :
            dp[i+jump][j] += dp[i][j]
        if j+jump < n:
            dp[i][j+jump] += dp[i][j]
print(dp[n-1][n-1])