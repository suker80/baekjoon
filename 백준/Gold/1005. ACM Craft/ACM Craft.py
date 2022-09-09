t = int(input())
from heapq import *
from collections import deque
for _ in range(t):
    n, k = map(int, input().split())
    time = list(map(int, input().split()))
    graph = [[] for _ in range(n)]
    degree = [0] * n
    dp = [0] * n

    for i in range(k):
        a, b = map(int, input().split())
        graph[a - 1].append(b - 1)
        degree[b - 1] += 1
    w = int(input())

    queue = deque()

    for i in range(n):
        if not degree[i]:
            queue.append(i)
            dp[i] = time[i]

    while queue:
        node = queue.popleft()

        for next in graph[node]:
            dp[next] = max(dp[next], dp[node] + time[next])
            degree[next] -= 1

            if not degree[next]:
                queue.append(next)
    print(dp[w-1])
