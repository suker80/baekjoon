from collections import defaultdict
from heapq import heappush, heappop

import sys
from time import time

input = sys.stdin.readline


def dijkstra(start):
    dist = defaultdict(lambda: float('inf'))
    dist[start] = 0

    heap = []
    trace = defaultdict(list)
    heap.append([0, start])
    while heap:
        cur_dist, cur = heappop(heap)
        for next in graph[cur].keys():
            cost = graph[cur][next]
            next_dist = cur_dist + cost

            if dist[next] == next_dist:
                trace[next].append(cur)
                continue

            if dist[next] > next_dist:
                dist[next] = next_dist
                trace[next].clear()
                trace[next].append(cur)
                heappush(heap, [next_dist, next])

    t = []
    t.extend(trace[destination])
    s = destination
    while t:
        while trace[s]:
            e= trace[s].pop()
            if graph[e].get(s):
                graph[e].pop(s)
            t.append(e)
        s = t.pop()


def almost_short(start):
    dist = defaultdict(lambda: float('inf'))
    dist[start] = 0

    heap = []
    heap.append([0, start])
    while heap:
        cur_dist, cur = heappop(heap)
        for next in graph[cur].keys():
            cost = graph[cur][next]
            next_dist = cur_dist + cost

            if dist[next] > next_dist:
                dist[next] = next_dist
                heappush(heap, [next_dist, next])

    return dist[destination]


while True:
    start_time = time()
    n, m = map(int, input().split())

    if n == 0 and m == 0:
        break

    start, destination = map(int, input().split())

    graph = defaultdict(lambda: defaultdict(int))

    for i in range(m):
        a, b, c = map(int, input().split())
        graph[a][b] = c

    dijkstra(start)
    short = almost_short(start)
    end_time = time()
    if short == float('inf'):
        print(-1)
    else:
        print(short)
    # print(end_time - start_time)