n = int(input())
import sys

sys.setrecursionlimit(10 ** 5)
max_level = 18
input = sys.stdin.readline
graph = [[] for _ in range(n + 1)]

parent = [[0] * max_level for _ in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

visit = [False] * (n+1)
depth = [0] * (n+1)

parent[0][0] = 0


def dfs(node, d):
    visit[node] = True
    depth[node] = d

    for vertex in graph[node]:

        if not visit[vertex]:
            parent[vertex][0] = node
            dfs(vertex, d + 1)


dfs(1, 1)
for i in range(1, 18):
        for j in range(1, n + 1):
            # 각 노드에 대해 2**i번째 부모 정보 갱신
            parent[j][i] = parent[parent[j][i - 1]][i - 1]
def lca(a, b):
    if depth[a] != depth[b]:

        if depth[b] > depth[a]:
            a, b = b, a

        for i in range(max_level-1,-1,-1):
            if depth[a] - depth[b] >= 2**i:
                a= parent[a][i]
    if a != b:

        for i in range(max_level - 1, -1, -1):

            if parent[a][i] != parent[b][i]:
                a = parent[a][i]
                b = parent[b][i]

            answer = parent[a][i]
    elif a== b:
        return a

    return answer


m = int(input())

for i in range(m):
    a, b = map(int, input().split())

    print(lca(a, b))
