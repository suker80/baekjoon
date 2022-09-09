from collections import deque

n, m, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append([b, True])
    graph[b].append([a, False])


def dfs(node, dir, subTree):
    visit[node] = True
    count = 1
    for next, iswin in graph[node]:     

        if not visit[next] and iswin == dir:
            count += dfs(next, dir,subTree)
    return count


visit = [False] * (n + 1)
result1 = dfs(x, False, 1)
visit = [False] * (n + 1)
result2 = dfs(x, True, 1)
print(result1,n-result2+1)
