n = int(input())

import sys

input = sys.stdin.readline
arr = list(map(int, input().split()))

graph = [[] for _ in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, input().split())

    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

dp = [[0] * 2 for _ in range(n)]  # 1은 포함 0 은 미포함

path = [[[] for _ in range(2)] for _ in range(n)]
for i in range(n):
    dp[i][1] = arr[i]

    path[i][1].append(i)
visit = [False] * n


def dfs(node):
    visit[node] = True

    for vertex in graph[node]:

        if not visit[vertex]:

            dfs(vertex)
            if dp[vertex][0] > dp[vertex][1]:
                dp[node][0] += dp[vertex][0]
                path[node][0] += path[vertex][0]
            else:
                dp[node][0] += dp[vertex][1]
                path[node][0] += path[vertex][1]

            dp[node][1] += dp[vertex][0]
            path[node][1] += path[vertex][0]
dfs(0)


if dp[0][0] > dp[0][1]:
    print(dp[0][0])
    for i in sorted(path[0][0]):
        print(i+1,end=' ')
else:
    print(dp[0][1])
    for i in sorted( path[0][1]):
        print(i+1,end=' ')