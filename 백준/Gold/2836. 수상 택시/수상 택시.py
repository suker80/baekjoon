n, m = map(int, input().split())
from heapq import *
import sys
input = sys.stdin.readline
inf = 10 ** 10
arr = []
for i in range(n):
    a, b = map(int, input().split())

    if a < b:
        continue

    else:
        arr.append([-a, -b])
arr.sort()
answer = 0
left, right = -inf, -inf
for i in range(len(arr)):
    cur_left, cur_right = arr[i]

    if cur_left > right:
        answer += (right - left) * 2
        left, right = cur_left, cur_right
    else:
        right = max(cur_right, right)
answer += (right - left) * 2
print(answer + m )
