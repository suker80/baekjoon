n = int(input())
import bisect
arr = list(map(int,input().split()))

dp = [arr[0]]
l = 1
for i in range(1,n):
    if dp[-1] < arr[i]:
        dp.append(arr[i])
        l+=1
    elif dp[-1]> arr[i]:
        idx = bisect.bisect_left(dp,arr[i])
        dp[idx] = arr[i]
print(l)