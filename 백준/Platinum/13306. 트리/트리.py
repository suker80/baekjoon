import sys
from collections import deque


def find(v):
    if parent[v] == v:
        return v
    else:
        parent[v] = find(parent[v])
        return parent[v]


def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return
    else:
        parent[x] = y


input = sys.stdin.readline
n, q = map(int, input().split())

orig_parent = list(range(n + 5))
parent = list(range(n + 5))
answer = deque()
query = []
orig_parent = list(range(n + 5))
for i in range(1, n):
    a = int(input())

    orig_parent[i + 1] = a

for i in range(n - 1 + q):
    query.append(list(map(int, input().split())))

for i in range(n - 1 + q):
    lst = query.pop()
    if lst[0] == 0:
        union(lst[1], orig_parent[lst[1]])
    else:
        x, y = lst[1], lst[2]
        answer.appendleft("YES") if find(x) == find(y) else answer.appendleft("NO")
print('\n'.join(answer))
