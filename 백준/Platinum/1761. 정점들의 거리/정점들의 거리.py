import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)


def dfs(node, d, w):
    visit[node] = True
    depth[node] = d
    weight[node] = w
    for vertex, vertex_weight in graph[node]:

        if not visit[vertex]:
            parent[vertex][0] = node
            dfs(vertex, d + 1, w + vertex_weight)


def lca(a, b):
    init_a, init_b = a, b
    if depth[a] != depth[b]:

        if depth[b] > depth[a]:
            a, b = b, a

        for i in range(max_level - 1, -1, -1):

            if depth[a] - depth[b] >= 2 ** i:
                a = parent[a][i]

    if a != b:
        for i in range(max_level - 1, -1, - 1):

            if parent[a][i] != parent[b][i]:
                a = parent[a][i]
                b = parent[b][i]
            LCA = parent[a][i]
    elif a == b:

        return weight[init_a] - weight[a] + weight[init_b] - weight[a]

    return weight[init_a] - weight[LCA] + weight[init_b] - weight[LCA]


if __name__ == '__main__':
    n = int(input())

    graph = [[] for _ in range(n + 1)]
    for i in range(n - 1):
        a, b, c = map(int, input().split())
        graph[a].append([b, c])
        graph[b].append([a, c])

    m = int(input())

    visit = [False] * (n + 1)
    depth = [0] * (n + 1)
    weight = [0] * (n + 1)
    max_level = 17
    parent = [[0] * max_level for _ in range(n + 1)]

    dfs(1, 1, 0)

    for i in range(1, max_level):
        for j in range(1, n + 1):
            # 각 노드에 대해 2**i번째 부모 정보 갱신
            parent[j][i] = parent[parent[j][i - 1]][i - 1]
    for i in range(m):
        a, b = map(int, input().split())

        print(lca(a, b))
