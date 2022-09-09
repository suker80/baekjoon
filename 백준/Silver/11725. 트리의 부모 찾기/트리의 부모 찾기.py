from collections import deque
n= int(input())

graph = [[] for _ in range(n+1)]
parent = [0] * (n+1)
for i in range(n-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

node = 1

visit = [False ] * (n+1)
queue = deque([node])

while queue:
    item = queue.popleft()


    for next_item in graph[item]:
        if visit[next_item] == False:
            visit[next_item] = True
            parent[next_item] = item
            queue.append(next_item)
for p in parent[2:]:
    print(p)

# def bfs(graph, start):