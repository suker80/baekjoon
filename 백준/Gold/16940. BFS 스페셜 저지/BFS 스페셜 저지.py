from collections import deque

n = int(input())

graph = [[] for _ in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
answer = list(map(int, input().split()))
visit = [False] * (n + 1)
depth = [0] * (n + 1)
parent = [0] * (n + 1)
order = [0] * (n + 1)
for i in range(n):
    order[answer[i]] = i


def dfs(node, d):
    visit[node] = True
    depth[node] = d

    for next in graph[node]:

        if not visit[next]:
            dfs(next, d + 1)
            parent[next] = node


dfs(1, 0)

for i in range(n - 1):

    if depth[answer[i]] > depth[answer[i+1]]:
        print(0)
        break
    if order[parent[answer[i]]] > order[parent[answer[i+1]]]:
        print(0)
        break
else:
    print(1)
