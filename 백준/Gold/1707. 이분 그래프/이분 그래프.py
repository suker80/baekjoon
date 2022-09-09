t = int(input())
import sys
from collections import deque

input = sys.stdin.readline


for _ in range(t):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    for i in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    visit = [-1] * (v + 1)
    res = 'YES'
    color = 1
    for i in range(v):
        if graph[i] and visit[i]== -1 :
            queue = deque([(i, color)])
            visit[i] = color
            while queue:
                n, color = queue.popleft()

                for k in graph[n]:
                    if visit[k] == -1:
                        visit[k] = (color + 1) % 2
                        queue.append((k, (color + 1) % 2))
                    elif visit[k] != -1 and visit[k] == color:
                        res = 'NO'

    print(res)