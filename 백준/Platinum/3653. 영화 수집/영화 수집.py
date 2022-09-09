import sys

input = sys.stdin.readline
t = int(input())


def init(node, left, right):
    if left == right:
        if left <= m:
            tree[node] = 0
        else:
            tree[node] = 1
        return tree[node]

    mid = (left + right) // 2
    m1 = init(node * 2, left, mid)
    m2 = init(node * 2 + 1, mid + 1, right)
    tree[node] = m1 + m2
    return tree[node]


def update(node, left, right, idx, diff):
    if left > idx or right < idx:
        return tree[node]

    if left == right and left == idx:
        tree[node] = diff
        return tree[node]

    mid = (left + right) // 2

    m1 = update(node * 2, left, mid, idx, diff)
    m2 = update(node * 2 + 1, mid + 1, right, idx, diff)

    tree[node] = m1 + m2
    return tree[node]


def query(node, left, right, start, end):
    if end < left or start > right:
        return 0

    if start <= left and end >= right:
        return tree[node]

    mid = (left + right) // 2

    m1 = query(node * 2, left, mid, start, end)
    m2 = query(node * 2 + 1, mid + 1, right, start, end)
    return m1 + m2


for _ in range(t):
    n, m = map(int, input().split())
    order = list(map(int, input().split()))
    point = m
    index = [m + i for i in range(n + 1)]
    tree = [0] * ((n + m) * 4)

    answer = []
    init(1, 1, n + m)
    for o in order:
        now = index[o]

        answer.append(query(1, 1, n + m, 1, now - 1))

        update(1, 1, n + m, now, 0)
        update(1, 1, n + m, point, 1)
        index[o] = point
        point -= 1
    print('\n'.join(map(str, answer)))
