import sys

input = sys.stdin.readline
n = int(input())

arr = [0] + list(map(int, input().split()))
m = int(input())

tree = [[] for _ in range(4 * n)]


# [odd , even ]
def init(left, right, node):
    if left == right:
        if arr[left] % 2 == 0:
            tree[node] = [0, 1]
        else:
            tree[node] = [1, 0]
        return tree[node]

    mid = (left + right) // 2

    m1_odd, m1_even = init(left, mid, node * 2)
    m2_odd, m2_even = init(mid + 1, right, node * 2 + 1)

    tree[node] = [m1_odd + m2_odd, m1_even + m2_even]
    return tree[node]


def update(left, right, node, index, val):
    if left == right and left == index:
        arr[index] = val

        if arr[left] % 2 == 0:
            tree[node] = [0, 1]
        else:
            tree[node] = [1, 0]

        return tree[node]

    if right < index or left > index:
        return tree[node]
    mid = (left + right) // 2

    m1_odd, m1_even = update(left, mid, node * 2, index, val)
    m2_odd, m2_even = update(mid + 1, right, node * 2 + 1, index, val)

    tree[node] = [m1_odd + m2_odd, m1_even + m2_even]
    return tree[node]


def query(left, right, node, i, j):
    if right < i or left > j:
        return [0, 0]

    if left >= i and right <= j:
        return tree[node]

    mid = (left + right) // 2

    m1_odd, m1_even = query(left, mid, node * 2, i, j)
    m2_odd, m2_even = query(mid + 1, right, node * 2 + 1, i, j)
    return [m1_odd + m2_odd, m1_even + m2_even]


init(1, n, 1)
for i in range(m):

    op, a, b = map(int, input().split())

    if op == 1:
        update(1, n, 1, a, b)
    elif op == 2:
        print(query(1, n, 1, a, b)[1])
    else:
        print(query(1, n, 1, a, b, )[0])
