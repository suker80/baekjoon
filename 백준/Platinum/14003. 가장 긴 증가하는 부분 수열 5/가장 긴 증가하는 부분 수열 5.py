n = int(input())
import bisect

arr = list(map(int, input().split()))

dp = [arr[0]]
d = [0] * n
l = 0
for i in range(1, n):
    if dp[-1] < arr[i]:
        dp.append(arr[i])
        l += 1
        d[i] = l
    else :
        idx = bisect.bisect_left(dp, arr[i])
        dp[idx] = arr[i]
        d[i] = idx

res = []

for i in range(n - 1, -1, -1):
    if d[i] == l:
        res.append(arr[i])
        l -= 1
res.reverse()
print(len(res))
print(*res)
