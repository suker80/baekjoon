n,m,k= map(int,input().split())
from collections import deque
cost = list(map(int,input().split()))

graph = [[] for _ in range(n)]

for _ in range(m):
    a,b = map(int,input().split())

    graph[a-1].append(b-1)
    graph[b - 1].append(a - 1)

visit = [False] * n

entire_cost = 0
def bfs(node):


    queue = deque([node])
    min_val = cost[node]
    while queue:
        current = queue.popleft()


        if not visit[current]:
            queue.extend(graph[current])
            min_val = min(min_val,cost[current])
            visit[current] = True

    return min_val
for i in range(n):
    if not visit[i]:
        c= bfs(i)
        entire_cost += c

if entire_cost <= k:
    print(entire_cost)
else:
    print('Oh no')