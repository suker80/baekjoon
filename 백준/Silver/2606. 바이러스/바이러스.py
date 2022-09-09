from collections import deque

n = int(input())
t = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(t):
    y, x = map(int,input().split())
    graph[y].append(x)
    graph[x].append(y)

visit = [False] * (n + 1)

queue = deque()
queue.extend(graph[1])
visit[1] = True
cnt = 0

while queue:
    n = queue.popleft()

    if visit[n] is False:
        cnt += 1
        queue.extend(graph[n])
        visit[n] = True
print(cnt)