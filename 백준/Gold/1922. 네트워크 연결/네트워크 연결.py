n = int(input())
m = int(input())
import sys
input = sys.stdin.readline
graph = [[float('inf')] * (n + 1) for _ in range(n + 1)]
for i in range(m):
    a, b, c = map(int,(input().split()))
    graph[a][b] = c
    graph[b][a] = c
visit = [False] * (n + 1)

distance = [float('inf')] * (n + 1)


def update_distance(node):
    for i in range(1,n+1):
        if not visit[i]:
            distance[i] = min(graph[node][i], distance[i])


def min_index(node):
    m = float('inf')
    idx = 0
    for i in range(1,n + 1):
        if not visit[i]:
            if distance[i] < m:
                m = distance[i]
                idx = i
    return idx


visit[1] = True
distance[1] = 0
node = 1

for i in range(n):
    update_distance(node)
    node = min_index(node)
    visit[node] = True


print(sum(distance[1:]))