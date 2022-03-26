import sys

input = sys.stdin.readline

n = int(input())

tree = [0] * (4 * n)
arr = [(int(input()), i + 1) for i in range(n)]

ranking = [0] * (n + 1)

for i, (v, r) in enumerate(sorted(arr, key=lambda x: x[0])):
    ranking[r] = i + 1


def update(node, start, end, idx):
    if start == end and start == idx:
        tree[node] += 1
        return tree[node]

    if start > idx or end < idx:
        return tree[node]

    mid = (start + end) // 2

    tree[node] = update(node * 2, start, mid, idx) + update(node * 2 + 1, mid + 1, end, idx)
    return tree[node]


def query(node, left, right, start, end):
    if left > end or right < start:
        return 0
    if start <= left and right <= end:
        return tree[node]

    mid = (left + right) // 2

    m1 = query(node * 2, left, mid, start, end)
    m2 = query(node * 2 + 1, mid + 1, right, start, end)
    return m1 + m2


ans = []
for i in range(n):
    rank = ranking[arr[i][1]]
    ans.append(i - query(1, 1, n, 1, rank) + 1)
    update(1, 1, n, rank)

print('\n'.join(map(str,ans)))