import sys

input = sys.stdin.readline
n, m = map(int, input().split())

arr = [0] * (n + 1)
fenwick = [0] * (n + 1)


def update(idx, val):
    diff = arr[idx] - val
    arr[idx] -= diff
    while idx <= n:
        fenwick[idx] -= diff

        idx += (idx & -idx)


def query(idx):
    res = 0
    while idx:
        res += fenwick[idx]
        idx -= (idx & -idx)
    return res


for i in range(m):
    op, a, b = map(int, input().split())

    if op:
        update(a, b)
    else:
        if b > a:
            print(query(b) - query(a - 1))
        else:
            print(query(a) - query(b-1))
