import sys

n, m = map(int, input().split())
input = sys.stdin.readline
from heapq import *

edge = []
for i in range(m + 1):
    a, b, c = map(int, input().split())
    edge.append([a, b, c])


def kruskal(reverse):
    edge.sort(reverse=reverse,key=lambda x:x[2])
    answer = 0

    def find(v):
        if parent[v] == v:
            return parent[v]
        else:
            parent[v] = find(parent[v])
        return parent[v]

    def union(a, b):
        p_a = find(a)
        p_b = find(b)

        if p_a > p_b:
            parent[p_a] = p_b
        else:
            parent[p_b] = p_a

    parent = list(range(n + 1))

    for i in range(m):
        a, b, c = edge[i]

        if find(a) != find(b):
            union(a, b)
            if c == 0:
                answer += 1
    return answer ** 2


print(kruskal(reverse=False) - kruskal(True))
