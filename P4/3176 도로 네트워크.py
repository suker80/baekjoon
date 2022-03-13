from collections import defaultdict
from math import log2
import sys

input = sys.stdin.readline
sys.setrecursionlimit(110000)
n = int(input())
size = int(log2(n) + 1)
graph = [[] for _ in range(n + 1)]
for i in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

visit = [False] * (n + 1)

depth = [0] * (n + 1)

parent = [[0] * size for _ in range(n + 1)]
parent_max = [[-float('inf')] * size for _ in range(n + 1)]
parent_min = [[float('inf')] * size for _ in range(n + 1)]

graph_max = [defaultdict(int) for _ in range(n + 1)]


def dfs(node):
    visit[node] = True

    for next, cost in graph[node]:
        if not visit[next]:
            depth[next] = depth[node] + 1
            dfs(next)
            parent[next][0] = node
            parent_max[next][0] = cost
            parent_min[next][0] = cost


dfs(1)
for j in range(1, size):
    for i in range(1, n + 1):
        parent[i][j] = parent[parent[i][j - 1]][j - 1]
        parent_max[i][j] = max(parent_max[i][j - 1], parent_max[parent[i][j - 1]][j - 1])
        parent_min[i][j] = min(parent_min[i][j - 1], parent_min[parent[i][j - 1]][j - 1])


def query(a, b):
    depth_a = depth[a]
    depth_b = depth[b]
    answer_max = -float('inf')
    answer_min = float('inf')
    if depth_a > depth_b:
        depth_diff = depth_a - depth_b
        while depth_diff:
            bit = int(log2(depth_diff))
            answer_max = max(parent_max[a][bit], answer_max)
            answer_min = min(parent_min[a][bit], answer_min)
            a = parent[a][bit]
            depth_diff -= 1 << bit
    elif depth_a < depth_b:
        depth_diff = depth_b - depth_a
        while (depth_diff):
            bit = int(log2(depth_diff))
            answer_max = max(parent_max[b][bit], answer_max)
            answer_min = min(parent_min[b][bit], answer_min)
            b = parent[b][bit]
            depth_diff -= 1 << bit
    if a == b:
        return answer_min, answer_max

    for i in range(size - 1, -1, -1):
        if parent[a][i] and parent[b][i]:
            if parent[a][i] != parent[b][i]:
                answer_max = max(answer_max, parent_max[a][i], parent_max[b][i])
                answer_min = min(answer_min, parent_min[a][i], parent_min[b][i])
                a = parent[a][i]
                b = parent[b][i]

    answer_max = max(answer_max, parent_max[a][0], parent_max[b][0])
    answer_min = min(answer_min, parent_min[a][0], parent_min[b][0])
    return answer_min, answer_max


k = int(input())
for i in range(k):
    a, b = map(int, input().split())
    print(*query(a, b))