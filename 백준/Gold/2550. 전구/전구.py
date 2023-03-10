n = int(input())
import bisect

arr = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
dp_len = []
dic = {}
for i, num in enumerate(arr2):
    dic[num] = i
arr3 = []
for num in arr:
    arr3.append(dic[num])

# 5 1 3 2 4
dp = [arr3[0]]
path = [0] * n
l = 0
for i in range(1, n):
    if dp[-1] < arr3[i]:
        dp.append(arr3[i])
        l += 1
        path[i] = l
    else:
        idx = bisect.bisect_left(dp, arr3[i])
        dp[idx] = arr3[i]
        path[i] = idx
ans_arr = []
for i in range(n - 1, -1, -1):
    if path[i] == l:
        ans_arr.append(arr3[i])
        l -= 1
print(len(dp))
answer = []
for i in range(len(dp)):
    answer.append(arr2[ans_arr[i]])
print(*sorted(answer))
