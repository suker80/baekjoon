import sys

sys.setrecursionlimit(500002)
input = sys.stdin.readline
n = int(input())
dp = [[0, 1] for _ in range(n + 1)]

graph = [[] for _ in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visit = [False] * (n + 1)


def dfs(node):
    visit[node] = True
    for next in graph[node]:
        if not visit[next]:
            dfs(next)
            dp[node][0] += dp[next][1]
            dp[node][1] += min(dp[next])


dfs(1)
print(min(dp[1]))
