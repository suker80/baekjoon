import sys
input = sys.stdin.readline
n, m, r = map(int, input().split())
from heapq import *

items = list(map(int, input().split()))

graph = [[] for _ in range(n)]
for i in range(r):
    a, b, c = map(int, input().split())
    graph[a - 1].append([b - 1, c])
    graph[b - 1].append([a - 1, c])

answer = 0


def solve(start):
    heap = []
    dist = [float('inf')] * n

    heappush(heap, [0, start])
    dist[start] = 0
    while heap:
        cur_dist, cur = heappop(heap)

        for next, next_dist in graph[cur]:
            nd = cur_dist + next_dist
            if dist[next] > nd and nd <= m:
                dist[next] = cur_dist + next_dist

                heappush(heap, [dist[next], next])
    item = sum([items[i] for i in range(n) if dist[i] != float('inf')])
    return item


for i in range(n):
    answer = max(solve(i), answer)
print(answer)
