import heapq
import sys
from heapq import *

input = sys.stdin.readline
n, m, k = map(int, input().split())
vertex = [0] * n
graph = [[] for _ in range(n)]
k_th = [0] * n
dist = [[-float('inf')] * k for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a - 1].append([b - 1, c])
    vertex[b - 1] += 1

dist[0][-1] = 0
k_th[0] = 1
heap = []
heap.append([0, 0])
while heap:
    current_dist, current = heappop(heap)

    for next, next_dist in graph[current]:
        total_dist = current_dist + next_dist
        if -dist[next][0] > total_dist:
            heappushpop(dist[next], -total_dist)
            heappush(heap, (total_dist, next))

for i in range(n):
    if dist[i][0] ==-float('inf'):
        print(-1)
    else:
        print(-dist[i][0])