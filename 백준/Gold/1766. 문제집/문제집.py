import sys
input = sys.stdin.readline
n,m = map(int,input().split())
graph=  [set() for _ in range(n+1)]
indegree = [0]*(n+1)
import heapq
for i in range(m):
    a,b = map(int,input().split())
    graph[a].add(b)
    indegree[b] += 1

answer = []
queue = []

for i in range(1,n+1):
    if indegree[i] == 0:
        queue.append(i)
while queue:
    cur = heapq.heappop(queue)
    print(cur,end=' ')
    for v in graph[cur]:
        indegree[v] -= 1

        if indegree[v] == 0:
            heapq.heappush(queue,v)

