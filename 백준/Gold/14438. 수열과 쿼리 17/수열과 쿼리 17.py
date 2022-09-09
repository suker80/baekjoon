n = int(input())

import math

import sys

input = sys.stdin.readline


arr = [float('inf')] + list(map(int, input().split()))

tree = [0] * (2 ** (math.ceil(math.log2(n)) +1 ))
m = int(input())


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

    if i<=left and right <= j:
        return tree[node]
    if right < i or left > j:
        return float('inf')
    mid = (left + right) // 2

    m1 = query(left, mid, node * 2,i,j)
    m2 = query(mid + 1, right, node * 2 + 1,i,j)


    return min(m1,m2)


def change(left, right, node, i, val):
    if not (left <= i and i <= right):
        return tree[node]

    if right == left and left == i:
        tree[node] = val
        return tree[node]

    mid = (left + right) // 2

    m1 = change(left, mid, node * 2, i, val)
    m2 = change(mid + 1, right, node * 2 +1 , i, val)

    tree[node] = min(m1,m2)

    return tree[node]
if __name__ == '__main__':

    init(1,n,1)
    for i in range(m):
        op, a, b = map(int, input().split())

        if op % 2 == 0:
            print(query(1,n,1,a, b))
        else:
            change(1,n,1,a, b)
