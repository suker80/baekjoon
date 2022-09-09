t = int(input())
import sys
input = sys.stdin.readline


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]
def union(a,b,p_a,p_b):
    parent[p_b] = p_a
    rank[p_a] += rank[p_b]


for _ in range(t):

    rank = dict()
    parent = dict()
    f = int(input())
    for i in range(f):
        a,b = input().rstrip().split()
        if a not in parent:
            parent[a] = a
            rank[a] = 1
        if b not in parent:
            parent[b] = b
            rank[b] = 1
        p_a ,p_b = find(a), find(b)

        if p_a != p_b:
            union(a,b,p_a,p_b)

        print(rank[p_a])

