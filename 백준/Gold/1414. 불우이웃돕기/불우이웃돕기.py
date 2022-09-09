n = int(input())
from heapq import *

graph = [list(input()) for _ in range(n)]

for i in range(n):
    for j in range(n):

        if ord(graph[i][j]) <= ord('Z') and graph[i][j] != '0':
            graph[i][j] = ord(graph[i][j]) - ord('A') + 27
        elif ord(graph[i][j]) >= ord('a'):
            graph[i][j] = ord(graph[i][j]) - ord('a') + 1
        elif graph[i][j] == '0':
            graph[i][j] = 0

graph_sum = sum([graph[i][j] for i in range(n) for j in range(n)])

parent = list(range(n))


def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])

    return parent[node]


def union(a, b):
    p_a = find(a)
    p_b = find(b)

    if p_a != p_b:
        parent[p_a] = p_b

tree_len = 0

def kruskal():
    heap = []
    global tree_len
    total_dist = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                heappush(heap, [graph[i][j], i, j])
    while heap:
        dist , a,b = heappop(heap)

        if find(a) != find(b):
            union(a,b)
            total_dist += dist
            tree_len += 1

    return total_dist
answer = graph_sum - kruskal()
print(answer) if tree_len >= n-1 else print(-1)


