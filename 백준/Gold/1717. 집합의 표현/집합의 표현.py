n, m = map(int, input().split())
parent = list(range(n+1))
import sys
input = sys.stdin.readline
print = sys.stdout.write
sys.setrecursionlimit(10000)
def find(n):
    if parent[n] != n:
        parent[n] = find(parent[n])
    return parent[n]


def union(r1, r2):

    r1 , r2 = find(r1),find(r2)

    if r1 < r2:
        parent[r1] = r2
    else:
        parent[r2]=r1
for i in range(m):
    op, a, b = map(int, input().split())

    if op == 0:
        union(a, b)
    elif op == 1:
        if find(a) == find(b):
            print("YES\n")
        else:
            print('NO\n')