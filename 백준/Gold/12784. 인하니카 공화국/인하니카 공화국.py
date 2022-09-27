def dfs(node, parent_weight):
    visit[node] = True

    if node and len(graph[node]) == 1:
        return graph[node][0][1]

    cost_sum = 0
    for next, cost in graph[node]:
        if not visit[next]:
            cost_sum += dfs(next, cost)

    return min(parent_weight, cost_sum)


t = int(input())

for testcase in range(t):

    n, m = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    visit = [False] * (n + 1)

    for i in range(m):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        graph[a].append([b, c])
        graph[b].append([a, c])

    print(dfs(0, float('inf')))
