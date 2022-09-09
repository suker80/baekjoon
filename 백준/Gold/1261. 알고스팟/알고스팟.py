m, n = map(int, input().split())
import heapq
graph = []
for i in range(n):
    graph.append([int(i) for i in input()])
direction = [(1, 0), (-1, 0), (0, -1), (0, 1)]
dist = [[float('inf')] * m for _ in range(n)]
dist[0][0] = 0

queue = []
heapq.heappush(queue,(0,(0,0)))
visit = [[0]*m for _ in range(n)]
visit[0][0] = 1
while queue:
    cnt ,( y,x) = heapq.heappop(queue)
    if y-1 == n and x-1 == m:
        break
    for dy,dx in direction:
        ny,nx = dy+y , dx+x
        if 0<=ny<n and 0<=nx<m and visit[ny][nx] == 0:
            dist[ny][nx] = cnt + graph[ny][nx]
            heapq.heappush(queue,(cnt+graph[ny][nx],(ny,nx)))
            visit[ny][nx] = 1
print(dist[n-1][m-1])