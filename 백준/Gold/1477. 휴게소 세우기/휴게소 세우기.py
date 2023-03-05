import math

n, m, l = map(int, input().split())

arr = list(map(int, input().split()))
arr.append(0), arr.append(l)
arr.sort()
left, right = 0, l
while left < right:
    mid = (left + right) // 2
    if not mid:
        left += 1
        break
    flag = True
    cnt = 0
    for i in range(len(arr) - 1):
        gap = arr[i + 1] - arr[i]
        if gap < mid:
            continue
        if gap % mid == 0:
            cnt += gap // mid - 1
        else:
            cnt += gap // mid
    if cnt > m:
        left = mid + 1
    else:
        right = mid
print(left)
