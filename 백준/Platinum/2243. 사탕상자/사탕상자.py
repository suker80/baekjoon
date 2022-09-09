import sys

input = sys.stdin.readline
n = int(input())
max_size = 1000000
candy = [0] * 1000001
fenwick = [0] * 1000001


def fenwick_update(idx, val):
    candy[idx] += val

    while idx <= max_size:
        fenwick[idx] += val
        idx += (idx & -idx)


def query(idx):
    res = 0
    while idx > 0:
        res += fenwick[idx]
        idx -= (idx & -idx)
    return res


def lower_bound(val):
    left, right = 1, 1000000

    while left < right:
        mid = (left + right) // 2
        if query(mid) > val:
            right = mid
        elif query(mid) == val:
            return mid

        else:
            left = mid + 1
    return right


for i in range(n):
    lst = list(map(int, input().split()))
    op = lst[0]

    if op == 2:
        a, b = lst[1], lst[2]
        fenwick_update(a, b)
    else:
        p = lst[1]
        idx = lower_bound(p)
        while query(idx) == query(idx - 1):
            idx -= 1
        print(idx)
        fenwick_update(idx, -1)
