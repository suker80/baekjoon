import sys

sys.setrecursionlimit(200000)
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

        if color_count[x] < color_count[y]:
            for e in color_set[x]:
                if not color_set[y].__contains__(e):
                    color_set[y].add(e)

                    color_count[y] += 1
            parent[x] = y
        else:
            color_set[x], color_set[y] = color_set[y], color_set[x]
            color_count[x], color_count[y] = color_count[y], color_count[x]
            for e in color_set[x]:
                if not color_set[y].__contains__(e):
                    color_set[y].add(e)
                    color_count[y] += 1
            parent[x] = y


input = sys.stdin.readline
n, q = map(int, input().split())

orig_parent = list(range(n + 5))
color_set = [set() for _ in range(n + 1)]
color_count = [0] * (n + 1)
parent = list(range(n + 5))
answer = deque()
query = []
orig_parent = list(range(n + 5))
for i in range(1, n):
    a = int(input())
    orig_parent[i + 1] = a
for i in range(n):
    a = int(input())
    color_set[i + 1].add(a)
    color_count[i + 1] = 1
for i in range(n - 1 + q):
    query.append(list(map(int, input().split())))

for i in range(n - 1 + q):
    lst = query.pop()
    if lst[0] == 1:
        union(lst[1], orig_parent[lst[1]])
    else:
        x = lst[1]
        answer.appendleft(color_count[find(x)])

print('\n'.join(map(str, answer)))
