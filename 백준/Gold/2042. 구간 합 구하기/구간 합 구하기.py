import sys
from math import ceil, log2

input = sys.stdin.readline
n, m, k = map(int, input().split())
arr = [0]
for i in range(n):
    arr.append(int(input()))

fenwick = [0] * (n + 1)

for i in range(1, n + 1):
    tmp = i & -i
    for j in range(tmp):
        fenwick[i] += arr[i-j]


def update(idx, val):
    diff = val - arr[idx]

    arr[idx] = val

    while idx <= n:
        fenwick[idx] += diff
        idx += (idx & - idx)


def query(x):
    ret = 0

    while x:
        ret += fenwick[x]
        x &= x - 1
    return ret


for i in range(m + k):
    op, a, b = map(int, input().split())

    if op % 2 == 1:
        update(a, b)
    else:
        print(query(b) - query(a-1))