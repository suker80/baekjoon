n = int(input())
import sys
input = sys.stdin.readline
parent = list(range(0, 1000001))
query = [1] * 1000001


def find(v):
    if parent[v] == v:
        return v
    else:
        parent[v] = find(parent[v])
        return parent[v]


def union(a, b):
    p_a, p_b = find(a), find(b)
    if p_a != p_b:
        parent[p_b] = parent[p_a]
        query[p_a] += query[p_b]
        query[p_b] = query[p_a]


for i in range(n):
    arr = input().split()

    if arr[0] == 'I':

        union(int(arr[1]), int(arr[2]))
    else:
        print(query[find(int(arr[1]))])
