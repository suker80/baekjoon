dp =[0] * 31
dp[0] = 1
dp[1] = 1
for i in range(2,31):

    for j in range(i):
        dp[i] += dp[i-j-1] * dp[j]
while True :
    n = int(input())
    if n==0:
        break
    print(dp[n])