import sys

input = sys.stdin.readline

n, q = map(int, input().split())

line = [list(map(int, input().split())) for _ in range(n)]

Q = [list(map(int, input().split())) for _ in range(q)]

parent = list(range(n + 1))


def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)
    parent[x] = y


max_idx = 0
max_right = line[0][1]
line.sort(key=lambda x: (x[1], x[0]))
for i in range(1, n):
    if max_right >= line[i][0]:
        max_right = line[i][1]
        union(max_idx, i)
    else:
        max_idx = i
        max_right = line[i][1]

for a, b in Q:
    print(1) if find(a - 1) == find(b - 1) else print(0)
