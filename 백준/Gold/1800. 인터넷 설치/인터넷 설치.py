n, m, k = map(int, input().split())
import sys

graph = [[] for _ in range(n)]
from heapq import *

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a - 1].append([b - 1, c])
    graph[b - 1].append([a - 1, c])


def dijkstra(thresh):
    start = 0
    dist = [float('inf')] * n
    dist[start] = 0

    heap = []
    heappush(heap, [start, 0])

    while heap:
        current_dist, current = heappop(heap)

        if current_dist > dist[current]:
            continue
        for next, next_weight in graph[current]:



            if next_weight <= thresh and current_dist < dist[next]:
                dist[next] = current_dist
                heappush(heap, [dist[next], next])

            elif next_weight > thresh and current_dist + 1 < dist[next]:
                dist[next] = current_dist + 1
                heappush(heap, [dist[next], next])
    return dist[n - 1] > k


left, right = 0, 1000000

answer = float('inf')
while left < right:
    mid = (left + right) // 2
    flag = dijkstra(mid)

    if not flag:
        right = mid
        answer = min(answer, mid)
    else:
        left = mid + 1

print(answer) if answer != float('inf') else print(-1)
