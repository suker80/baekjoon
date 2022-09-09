def update(left, right, node, i, val):
    if left == right and left == i:
        tree[node] += val
        return tree[node]

    if right < i or left > i: return tree[node]

    mid = (left + right) // 2

    m1 = update(left, mid, node * 2, i, val)
    m2 = update(mid + 1, right, node * 2 + 1, i, val)

    tree[node] = m1 + m2

    return tree[node]


def query(left, right, node, i, j):
    if left >= i and right <= j:
        return tree[node]
    if right < i or left > j:
        return 0

    mid = (left + right) // 2

    m1 = query(left, mid, node * 2, i, j)
    m2 = query(mid + 1, right, node * 2 + 1, i, j)

    return m1 + m2


if __name__ == '__main__':
    import sys
    import math

    input = sys.stdin.readline

    n, m = map(int, input().split())

    tree = [0] *  (1 <<(math.ceil(math.log2(n)) + 1))

    for i in range(m):

        op, a, b = map(int, input().split())

        if op % 2==0:
            res = query(1, n, 1, a, b)
            print(res)
        else:
            update(1, n, 1, a, b)
