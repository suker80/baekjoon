n, m = map(int, input().split())
univ = input().split()
from heapq import *

graph = [[] for _ in range(n)]
for i in range(m):
    u, v, d = map(int, input().split())

    graph[u - 1].append([v - 1, d])
    graph[v - 1].append([u - 1, d])


def prim():
    answer = 0
    here = 0
    visit = [False] * n
    visit[here] = True
    heap = []
    for next, dist in graph[here]:
        if univ[here] != univ[next]:
            heappush(heap, [dist, next])
    while heap:
        here_dist, here = heappop(heap)
        if not visit[here]:
            answer += here_dist
            visit[here] = True
            for next, dist in graph[here]:
                if univ[here] != univ[next]:
                    heappush(heap, [dist, next])
        else:
            continue
    if sum(visit) == n :
        return answer
    else:
        return -1 
    
print(prim())


