n = int(input())
import sys
input = sys.stdin.readline

start = list(map(int,input().split()))

max_dp = start[:]
min_dp = start[:]

for i in range(1,n):
    a,b,c= list(map(int,input().split()))

    temp_max =[0,0,0]
    temp_min = [0, 0, 0]

    temp_max[0] = max(max_dp[0],max_dp[1]) + a
    temp_max[1] = max(max_dp[0], max_dp[1],max_dp[2]) + b
    temp_max[2] = max(max_dp[1], max_dp[2]) + c

    max_dp = temp_max[:]

    temp_min[0] = min(min_dp[0],min_dp[1]) + a
    temp_min[1] = min(min_dp[0], min_dp[1],min_dp[2]) + b
    temp_min[2] = min(min_dp[1], min_dp[2]) + c

    min_dp = temp_min[:]

print(max(max_dp),min(min_dp))