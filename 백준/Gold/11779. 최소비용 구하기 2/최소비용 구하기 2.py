n = int(input())
m = int(input())

import sys
import heapq
input = sys.stdin.readline
from collections import defaultdict

def default_dict():

    return float('inf')
graph = [defaultdict(default_dict) for _ in range(n+1)]
heap =[]
distance = [float('inf') ] * (n+1)
for i in range(m):
    a,b,c = map(int,input().split())

    graph[a][b] = min(graph[a][b],c)

def dijkstra(start,end ):

    heap = []
    path = [start]
    distance[start] = 0
    heapq.heappush(heap,[0,start,path])

    while heap:
        current_dist, here,temp_path =heapq.heappop(heap)

        for next_city , dist in graph[here].items():
            next_dist = distance[here] + dist

            if next_dist < distance[next_city]:
                distance[next_city] = next_dist
                if next_city == end:
                    path = temp_path + [next_city]
                heapq.heappush(heap,[next_dist,next_city,temp_path + [next_city]])

    return distance,path




start,end = map(int,input().split())
dist,path = dijkstra(start,end)
print(dist[end])
print(len(path))
print(*path)
