# import sys
# from math import ceil, log2
#
# input = sys.stdin.readline
# n, m, k = map(int, input().split())
# arr = [0]
# for i in range(n):
#     arr.append(int(input()))
#
# fenwick = [0] * (n + 1)
#
# for i in range(1, n + 1):
#     tmp = i & -i
#     for j in range(tmp):
#         fenwick[i] += arr[i - j]
#
#
# def update(start, end, val):
#     arr[idx] += val
#
#     while idx <= n:
#         fenwick[idx] += val
#         idx += (idx & - idx)
#
#
# def query(x):
#     ret = 0
#
#     while x:
#         ret += fenwick[x]
#         x &= x - 1
#     return ret
#
#
# for i in range(m + k):
#     lst = list(map(int, input().split()))
#     op = lst[0]
#
#     if op == 1:
#         a, b, c = lst[1], lst[2], lst[3]
#         update(a, b, c)
#     else:
#         a, b = lst[1], lst[2]
#         print(query(b) - query(a - 1))


import sys
from math import ceil, log2

input = sys.stdin.readline

n, m, k = map(int, input().split())

arr = [0] + [int(input()) for _ in range(n)]
max_size = n*4
tree = [0] * max_size
lazy = [0] * max_size


def init(left, right, node):
    if left == right:
        tree[node] = arr[left]
        return tree[node]

    mid = (left + right) // 2

    m1 = init(left, mid, node * 2)
    m2 = init(mid + 1, right, node * 2 + 1)
    tree[node] = m1 + m2

    return tree[node]


def update(left, right, node, i, j, val):

    if lazy[node] != 0:
        tree[node] += lazy[node] * (right - left + 1)
        if left != right:
            lazy[node * 2 + 1] += lazy[node]
            lazy[node * 2] += lazy[node]
        lazy[node] = 0

    if right < i or left > j:
        return tree[node]
    if i <= left and j >= right:
        tree[node] += val * (right - left + 1)
        if left != right:
            lazy[node * 2] += val
            lazy[node * 2 + 1] += val

        return tree[node]

    mid = (left + right) // 2
    m1 = update(left, mid, node * 2, i, j, val)
    m2 = update(mid + 1, right, node * 2 + 1, i, j, val)

    tree[node] = m1 + m2
    return tree[node]


def query(left, right, node, i, j):
    if right < i or left > j:
        return 0
    if lazy[node] != 0:
        tree[node] += lazy[node] * (right - left + 1)
        if left != right:
            lazy[node * 2 + 1] += lazy[node]
            lazy[node * 2] += lazy[node]
        lazy[node] = 0
    if i <= left and j >= right:
        return tree[node]

    mid = (left + right) // 2
    m1 = query(left, mid, node * 2, i, j)
    m2 = query(mid + 1, right, node * 2 + 1, i, j)

    return m1 + m2


init(1, n, 1)
for i in range(m + k):
    lst = list(map(int, input().split()))
    op = lst[0]

    if op == 1:
        a, b, c = lst[1:]
        update(1, n, 1, a, b, c)
    else:
        a, b = lst[1:]
        print(query(1, n, 1, a, b))
