from bisect import *

n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, n + 1
answer = 0
answer_idx = []
while left < right:
    temp = [0]
    mid = (left + right) // 2
    idx = 0
    cur = arr[0]
    while idx < k:
        i = bisect_left(arr, mid + cur)

        if i >= k:
            break
        temp.append(i)
        cur = arr[i]
    if len(temp) < m:
        right = mid
        continue
    if len(temp) >= m:
        left = mid + 1
        answer_idx = temp
        continue
answer = ['0'] * k
for i in answer_idx[:m]:
    answer[i] = '1'
print(''.join(answer))
