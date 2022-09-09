import sys

input = sys.stdin.readline
import math


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


def kruskal():
    cost = 0

    for i in range(len(edges)):

        c, a, b = edges[i]
        if find(a) != find(b):
            union(a, b)
            cost += c

    return cost


if __name__ == '__main__':
    n, m = map(int, input().split())
    parent = list(range(n))
    edges = []
    point = []
    for i in range(n):
        a, b = map(int, input().split())
        point.append([a, b])

    for i in range(n-1):
        for j in range(i + 1, n):
            x1, y1 = point[i]
            x2, y2 = point[j]
            dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            edges.append([dist, i, j])
    for i in range(m):
        a, b = map(int, input().split())
        union(a - 1, b - 1)
    edges.sort(key=lambda x: x[0])
    print(format(kruskal(), ".2f"))