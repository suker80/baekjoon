import sys
input = sys.stdin.readline
n,m = [int(_) for _ in input().split(' ')]
graph = [[] for i in range(n+1)]
for i in range(m):
    u,m = [int(_) for _ in input().split(' ')]
    graph[u].append(m)
    graph[m].append(u)

from collections import deque
def bfs(graph,start):
    visit = set([])
    queue = deque([start])
    while queue:
        n = queue.popleft()
        if n not in visit:
            visit.add(n)
            queue.extendleft(graph[n])
    return visit

not_visit = set(range(1,n+1))
count = 0
while not_visit:
    start = not_visit.pop()
    visit = bfs(graph,start)
    count += 1
    not_visit = not_visit.difference(visit)

print(count)