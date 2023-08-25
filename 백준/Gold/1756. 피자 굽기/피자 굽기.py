import bisect
from bisect import *
d, n = map(int, input().split())

oven = list(map(int, input().split()))
pizza = list(map(int, input().split()))
answer = 0
last_idx = -1
arr= [0] * d
temp = float('inf')
if d== 1:
    if oven[0] >= pizza[0]:
        print(1)
    else:
        print(0)
    exit()
for i,o in enumerate(oven):
    temp = min(temp,o)
    arr[i] = temp

arr.reverse()
for p in pizza:
    last_idx = bisect_left(arr,p,last_idx + 1)

print(max(0,d - last_idx))