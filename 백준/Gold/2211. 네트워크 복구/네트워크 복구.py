n,m = map(int,input().split())
import sys
from heapq import heappop,heappush
input = sys.stdin.readline
from collections import defaultdict
def default_dict():

    return float('inf')
graph = [defaultdict(default_dict) for _ in range(n)]
for i in range(m):
    a,b,c = map(int,input().split())
    graph[a-1][b-1] = c
    graph[b-1][a-1] = c


def djisktra(start = 0 ):
    distance = [float('inf')] * n
    distance[start] = 0
    heap = []
    heappush(heap,[0,start])
    dist_path = [0] * n
    while heap:
        current, here = heappop(heap)

        for next_city,dist in graph[here].items():

            next_dist = current + dist

            if distance[next_city] > next_dist:
                heappush(heap,[next_dist,next_city])
                dist_path[next_city] = [here+1,next_city+1]
                distance[next_city] = next_dist
    return dist_path

answer = djisktra(0)
print(n-1)
for i in range(1,n):
    print(*answer[i])