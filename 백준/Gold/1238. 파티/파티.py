n,m,x = map(int,input().split())

import sys
import heapq
input = sys.stdin.readline
from collections import defaultdict
def _default():
    return float('inf')
graph = [defaultdict(_default) for _ in range(n+1)]

for i in range(m):
    a,b,c = map(int,input().split())

    graph[a][b] = c


def dijkstra(start):
    distance = [float('inf') ]* (n+1)
    heap = []
    distance[start] = 0

    heapq.heappush(heap,[0,start])
    while heap:
        current_dist , current = heapq.heappop(heap)

        for next_road , dist in graph[current].items():
            next_dist  = dist + current_dist

            if next_dist < distance[next_road]:
                distance[next_road] = next_dist

                heapq.heappush(heap,[next_dist,next_road])

    return distance

answer = 0
back = dijkstra(x)
for i in range(1,n+1):
    go = dijkstra(i)[x]


    answer = max(answer, go+back[i])

print(answer)




