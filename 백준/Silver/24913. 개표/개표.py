import sys
import math
input = sys.stdin.readline
n, q = map(int, input().split())

arr = [0] * (n + 1)
counts = 0
m = 0
for i in range(q):
    lst = list(map(int, input().split()))
    if lst[0] == 1:
        arr[lst[2] - 1] += lst[1]
        if lst[2] != n + 1:
            counts += lst[1]
            m = max(m, arr[lst[2] - 1])
    else:
        print("YES") if arr[-1] + lst[1] > max(m, math.ceil((counts + lst[2]) / n)) else print("NO")
