import sys

input = sys.stdin.readline

n = int(input())

arr = [0] + list(map(int, input().split()))

m = int(input())
tree = [0] * (n * 4)
lazy = [0] * (n * 4)
answer = []


def init(node, left, right):
    if left == right:
        tree[node] = arr[left]
        return

    mid = (left + right) // 2

    init(node * 2, left, mid)
    init(node * 2 + 1, mid + 1, right)


def update(node, left, right, start, end, diff):
    if left >= start and right <= end:
        lazy[node] += diff
        return
    if left > end or start > right:
        return
    mid = (left + right) // 2

    update(node * 2, left, mid, start, end, diff)
    update(node * 2 + 1, mid + 1, right, start, end, diff)


def query(node, left, right, index, diff):
    diff += lazy[node]
    if index < left or index > right:
        return 0

    if left == right and left == index:
        answer.append(tree[node] + diff)
        return

    mid = (left + right) // 2

    query(node * 2, left, mid, index, diff)
    query(node * 2 + 1, mid + 1, right, index, diff)


init(1, 1, n)

for i in range(m):
    lst = list(map(int, input().split()))

    if lst[0] == 1:
        update(1, 1, n, lst[1], lst[2], lst[3])
    else:
        query(1, 1, n, lst[1], 0)

print('\n'.join(map(str, answer)))
