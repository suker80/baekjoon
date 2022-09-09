from bisect import *

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
answer = float('inf')
answer_idx = []
for i in range(n):
    for j in range(i + 1, n):
        temp = arr[i] + arr[j]
        left = bisect_right(arr, -temp, )
        if left == n:
            left -= 1

        if i == left or j == left:
            continue

        if answer > abs(temp + arr[left]):
            answer = abs(temp + arr[left])
            answer_idx = [arr[i], arr[j], arr[left]]

        left -= 1

        if i == left or j == left:
            continue

        if answer > abs(temp + arr[left]):
            answer = abs(temp + arr[left])
            answer_idx = [arr[i], arr[j], arr[left]]
print(*sorted(answer_idx))
