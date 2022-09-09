t = int(input())

import sys

input = sys.stdin.readline


def dfs(node):
    if visit[node] == 1: return
    visit[node] = 1

    for i in graph[node]:
        if dfs(d[i]) or  d[i] == -1:
            d[i] = node
            return True
    return False



for _ in range(t):
    n, m = map(int, input().split())

    graph = [[] for _ in range(m)]

    answer = 0
    d = [-1] * n

    for i in range(m):
        a,b  = map(int,input().split())

        graph[i] = list(range(a-1,b))

    for i in range(m):
        visit = [0] * (m)

        if dfs(i):
            answer += 1

    print(answer)
