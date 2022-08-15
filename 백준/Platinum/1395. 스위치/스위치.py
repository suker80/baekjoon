def update(node, left, right, s, t):
    if lazy[node]:
        if left != right:
            lazy[node * 2] += lazy[node]
            lazy[node * 2 + 1] += lazy[node]
        if lazy[node] % 2:
            tree[node] = (right - left + 1) - tree[node]
        lazy[node] = 0
    if s <= left and right <= t:
        lazy[node] += 1
        if lazy[node] % 2:
            tree[node] = (right - left + 1) - tree[node]
            if left != right:
                lazy[node * 2] += lazy[node]
                lazy[node * 2 + 1] += lazy[node]
            lazy[node] = 0
        return tree[node]
    if left > t or right < s:
        return tree[node]
    mid = (left + right) // 2
    m1 = update(node * 2, left, mid, s, t)
    m2 = update(node * 2 + 1, mid + 1, right, s, t)
    tree[node] = m1 + m2
    return tree[node]


def query(node, left, right, s, t):
    if lazy[node]:
        if left != right:
            lazy[node * 2] += lazy[node]
            lazy[node * 2 + 1] += lazy[node]
        if lazy[node] % 2:
            tree[node] = (right - left + 1) - tree[node]
        lazy[node] = 0

    if s <= left and right <= t:
        return tree[node]

    if left > t or right < s:
        return 0

    mid = (left + right) // 2
    m1 = query(node * 2, left, mid, s, t)
    m2 = query(node * 2 + 1, mid + 1, right, s, t)
    return m1 + m2


if __name__ == '__main__':
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    tree = [0] * (n * 4)
    lazy = [0] * (n * 4)
    answer = []
    for i in range(m):

        o, s, t = map(int, input().split())
        if o:
            print(query(1, 1, n, s, t))
        else:
            update(1, 1, n, s, t)
    # print('\n'.join(map(str, answer)))
