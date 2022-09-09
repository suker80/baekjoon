n= int(input())

p = list(map(int,input().split()))

dp = [p[0]]
dp.append(max(p[0]*2,p[1]))

dp

for i in range(2,n):
    max_val = 0
    for j in range(0,i):
        max_val = max(max_val,p[i],dp[j]+dp[i-j-1])
    dp.append(max_val)

print(dp[-1])