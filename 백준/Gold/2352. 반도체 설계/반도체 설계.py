n = int(input())

arr = list(map(int, input().split()))

dp = [arr[0]]
import bisect

for i in range(1, n):
    if dp[-1] < arr[i]:
        dp.append(arr[i])
    else:
        idx = bisect.bisect_left(dp, arr[i])
        dp[idx] = arr[i]
print(len(dp))

