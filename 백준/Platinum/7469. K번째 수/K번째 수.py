from bisect import *

n, q = map(int, input().split())
arr = [0] + list(map(int, input().split()))
tree = [0] * (4 * n)


def init(left, right, node):
    if left == right:
        tree[node] = [arr[left]]
        return tree[node]

    mid = (left + right) // 2

    l = init(left, mid, node * 2)
    r = init(mid + 1, right, node * 2 + 1)

    tree[node] = sorted(l + r)
    return tree[node]


def query(left, right, node, start, end, k):
    if left > end or right < start:
        return 0

    if start <= left and right <= end:
        return bisect(tree[node], k)

    mid = (left + right) // 2

    l = query(left, mid, node * 2, start, end, k)
    r = query(mid + 1, right, node * 2 + 1, start, end, k)
    return l + r


init(1, n, 1)
answer = []
for _ in range(q):
    i, j, k = map(int, input().split())
    left, right = -10 ** 9, 10 ** 9
    answer = float('inf')
    while left < right:
        mid = (left + right) // 2
        count = query(1, n, 1, i, j, mid)
        if count == k:
            answer = min(answer, mid)
            right = mid
        elif count > k:
            right = mid
        else:
            left = mid + 1
    print(answer)
