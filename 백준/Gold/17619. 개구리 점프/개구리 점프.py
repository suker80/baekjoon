import sys
sys.setrecursionlimit(100001)
input = sys.stdin.readline

n, q = map(int, input().split())

line = [list(map(int, input().split())) + [_ + 1] for _ in range(n)]

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


line.sort()

line_idx = line[0][3]
line_left = line[0][0]
line_right = line[0][1]
for i in range(1, n):
    if line_right >= line[i][0]:
        line_right = max(line[i][1], line_right)
        union(line_idx, line[i][3])
    else:
        line_right = line[i][1]
        line_idx = line[i][3]

for a, b in Q:
    print(1) if find(a) == find(b) else print(0)
