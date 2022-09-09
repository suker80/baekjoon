import sys
from heapq import *

sys.setrecursionlimit(100000)
input = sys.stdin.readline


def kruskal():
    def find(v):
        if parent[v] == v:
            return v
        parent[v] = find(parent[v])
        return parent[v]

    def union(a, b):
        pa, pb = find(a), find(b),

        if pa > pb:
            parent[pb] = pa
        elif pa < pb:
            parent[pa] = pb

    cnt = m - 1
    cost = 0
    parent = list(range(m))

    for i in range(n):
        if not cnt:
            break
        a, b, c = edges[i]
        if find(a) != find(b):
            union(a, b)
            cost += c


    return cost


while True:

    m, n = map(int, input().split())
    if not m and not n: break

    edges = []
    s = 0
    for i in range(n):
        a, b, c = map(int, input().split())

        edges.append([a, b, c])
        s +=c
    edges.sort(key=lambda x: x[2])

    print(s - kruskal())
