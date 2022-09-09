n, m, k = map(int, input().split())

import sys
from heapq import heappop, heappush

input = sys.stdin.readline

graph = [[] for _ in range(n)]

visit = [0] * n
for i in range(m):
    a, b, c = map(int, input().split())

    graph[a - 1].append([b - 1, c])
    graph[b - 1].append([a - 1, c])

dist = [[float('inf')] * n for _ in range(k + 1)]


def dijkstra():
    for i in range(k+1):
        dist[i][0] = 0


    heap = []

    heappush(heap, [0, 0, k])

    while heap:
        cost, here, wrap = heappop(heap)

        if dist[wrap][here] <cost:
            continue

        for next, d in graph[here]:
            next_cost = d + cost

            if next_cost < dist[wrap][next]:
                dist[wrap][next] = next_cost
                heappush(heap,[next_cost, next, wrap])
            if wrap > 0 and cost < dist[wrap - 1][next]:
                dist[wrap - 1][next] = cost
                heappush(heap,[cost, next, wrap - 1])


dijkstra()

answer= float('inf')

for i in range(k+1):
    answer = min(dist[i][-1],answer)

print(answer)
