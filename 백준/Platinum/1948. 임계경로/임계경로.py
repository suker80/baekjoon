import sys
from collections import deque, defaultdict

input = sys.stdin.readline

n = int(input())
m = int(input())

indegree = defaultdict(int)
rev_indegree = defaultdict(int)
graph = [[] for _ in range(n + 1)]
rev_graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    indegree[b] += 1
    rev_graph[b].append([a, c])
    rev_indegree[a] += 1

start, end = map(int, input().split())

dist = [0] * (n + 1)
queue = deque([start])
while queue:

    here = queue.popleft()
    for next_city, cost in graph[here]:
        dist[next_city] = max(dist[next_city], dist[here] + cost)
        indegree[next_city] -= 1

        if indegree[next_city] == 0:
            queue.append(next_city)

queue = deque([end])
answer = 0
check = [False] * (n + 1)
check[end] = True
while queue:

    here = queue.popleft()

    for next_city, cost in rev_graph[here]:

        if check[here] and dist[here] - cost == dist[next_city]:
            answer += 1
            check[next_city] = True
        rev_indegree[next_city] -= 1

        if rev_indegree[next_city] == 0:
            queue.append(next_city)
print(dist[end])
print(answer)
