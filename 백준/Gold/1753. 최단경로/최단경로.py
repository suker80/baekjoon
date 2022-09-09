import sys

v, e = map(int, input().split())
input = sys.stdin.readline
from heapq import *

start = int(input())

graph = [[] for _ in range(v)]

for i in range(e):
    a, b, c = map(int, input().split())
    graph[a - 1].append([b - 1, c])

dist = [float("inf")] * v
dist[start - 1] = 0

heap = []

heappush(heap, [0, start - 1])

while heap:
    dist_here, here = heappop(heap)

    for next, next_dist in graph[here]:

        if dist_here + next_dist < dist[next]:
            dist[next] = dist_here + next_dist
            heappush(heap, [dist_here + next_dist, next])
for i in range(v):
    if dist[i] < float('inf'):
        print(dist[i])
    else:
        print("INF")
