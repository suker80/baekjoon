n, m = map(int, input().split())

import sys
from heapq import heappop, heappush

input = sys.stdin.readline

liter = list(map(int, input().split()))

graph = [[] for _ in range(n)]

for i in range(m):
    a, b, c = map(int, input().split())

    graph[a - 1].append([b - 1, c])
    graph[b - 1].append([a - 1, c])


def dijkstra():
    dist = [[float('inf')] * n for _ in range(2501)]
    oil = liter[0]
    dist[oil][0] = 0
    visit = [[False] * n for _ in range(2501)]
    visit[oil][0] = True

    heap = []

    heappush(heap, [0, 0, oil])
    while heap:
        current, here, oil = heappop(heap)

        if here == n - 1:
            return current

        visit[oil][here] = True
        for next, weight in graph[here]:

            if not visit[oil][next]:
                cost = current + oil * weight

                heappush(heap, [cost, next, min(oil, liter[next])])


print(dijkstra())
