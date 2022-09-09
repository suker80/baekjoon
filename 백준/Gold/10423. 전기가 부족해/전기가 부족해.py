n,m,k = map(int,input().split())
import sys
from heapq import heappop,heappush
input = sys.stdin.readline
graph= [[] for _ in range(n)]

power_plant = list(map(int,input().split()))

visit = [False] * n


for i in range(m):
    a,b,c = map(int,input().split())
    graph[a-1].append([b-1,c])
    graph[b-1].append([a-1,c])

heap = []

dist= [float('inf')] * n
for p in power_plant:
    visit[p-1] = True
    for v,c in graph[p-1]:
        heappush(heap,[c,v])
        dist[v] = min(dist[v],c)
answer= 0
while heap:
    cost,next_node = heappop(heap)

    if not visit[next_node]:
        answer += cost
        visit[next_node] = True

        for v,c in graph[next_node]:
            if not visit[v]:
                heappush(heap,[c,v])

print(answer)

