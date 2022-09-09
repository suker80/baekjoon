n = int(input())
import sys
wine = [int(input())for i in range(n)]
if len(wine) <3 :
    print(sum(wine))
    sys.exit()
dp = [wine[0],wine[0] + wine[1]]
dp.append(max(dp[0] + wine[2] , dp[1],wine[1]+wine[2]))


for i in range(3,n):
    dp.append(
    max(
        dp[i-3] + wine[i-1] + wine[i],
        dp[i-1],
        dp[i-2] + wine[i]
    
    
    )
    
    )
print(max(dp))    