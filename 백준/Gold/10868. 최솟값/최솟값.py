n, m = map(int, input().split())
import sys
from math import ceil, log2

inf = float('inf')
input = sys.stdin.readline
arr = [0]
tree = [inf] * (1 << (ceil(log2(n)) + 1))
for i in range(n):
    arr.append(int(input()))


def init(left, right, node):
    if left == right:
        tree[node] = arr[left]
        return tree[node]

    mid = (left + right) // 2
    m1 = init(left, mid, node * 2)
    m2 = init(mid + 1, right, node * 2 + 1)

    tree[node] = min(m1, m2)
    return tree[node]


def query(left, right, node, i, j):
    if right < i or left > j:
        return inf
    if i <= left and right <= j:
        return tree[node]

    mid = (left + right) // 2

    m1 = query(left, mid, node * 2, i, j)
    m2 = query(mid + 1, right, node * 2 + 1, i, j)

    return min(m1, m2)


# def update(left, right, node, idx, val):
#     if left == right and left == idx:
#         tree[node] = val
#         return tree[node]
#
#     mid = (left + right) // 2
#     m1 = update(left, mid, node * 2, idx, val)
#     m2 = update(mid + 1, right, node * 2 + 1, idx, val)
#
#     tree[node] = min(m1, m2)
#     return tree[node]
init(1, n, 1)
answer= []
for i in range(m):
    a, b = map(int, input().split())
    if a > b:
        answer.append(query(1, n, 1, b, a))
    else:
        answer.append(query(1, n, 1, a, b))
        
print('\n'.join(map(str,answer)))
