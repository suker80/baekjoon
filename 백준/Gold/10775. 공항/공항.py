import sys
input = sys.stdin.readline
G = int(input())
p = int(input())

g = [int(input()) for _ in range(p)]
parent = list(range(G + 1))
answer = 0


def find(v):
    if parent[v] == v:
        return v
    parent[v] = find(parent[v])
    return parent[v]


def union(a, b):
    a = find(a)
    b = find(b)

    parent[a] = b


for i in g:
    if find(i):
        union(i, find(i) -1)
        answer +=1
    else:
        break
print(answer)
