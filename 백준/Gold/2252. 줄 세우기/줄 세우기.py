n,m = map(int,input().split())

import sys

from collections import deque
input = sys.stdin.readline
graph=  [set() for _ in range(n+1)]
parent = list(range(0,n+1))
reverse_graph = [set() for _ in range(n+1)]
for i in range(m):
    b,a = map(int,input().split())
    graph[a].add(b)
    reverse_graph[b].add(a)


queue = deque()
answer = []
for i in range(1,n+1):
    if not graph[i]:
        queue.append(i)


visit = [False] * (n+1)

while queue:

    temp_queue = deque([queue.popleft()])
    while temp_queue:
        current = temp_queue.popleft()
        print(current,end=' ')
        visit[current] = True
        for v in reverse_graph[current]:
            graph[v].discard(current)
            if not graph[v]:
                temp_queue.append(v)

