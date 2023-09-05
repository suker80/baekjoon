n, m = map(int, input().split())
import sys
sys.setrecursionlimit(112346)
company = list(map(int, input().split()))

graph = [[] for _ in range(n + 1)]
dp = [0] * (n + 1)
answer = [0] * (n + 1)
visit = [False] * (n + 1)
for i in range(m):
    j, w = map(int, input().split())
    dp[j] += w

tree = [[] for _ in range(n + 1)]

for i in range(1, n):
    tree[company[i]].append(i + 1)


def dfs(node):
    for next_node in tree[node]:
        dp[next_node] += dp[node]
        dfs(next_node)


dfs(1)

print(*dp[1:])
