from heapq import heappop, heappush
from math import sqrt, pow

a = list(map(float, input().split()))
b = list(map(float, input().split()))

n = int(input())

edge = [list(map(float, input().split())) for _ in range(n)]
edge = [a] + edge + [b]
graph = [[float("inf")] * (n + 2) for _ in range(n + 2)]


def calc(point_1, point_2):
    return sqrt(pow(point_1[0] - point_2[0], 2) + pow(point_1[1] - point_2[1], 2))


for i in range(n + 2):
    for j in range(i + 1, n + 2):
        if i == j: continue

        if i == 0:
            graph[i][j] = calc(edge[i], edge[j]) / 5
            graph[j][i] = graph[i][j]

        else:
            ij_dist = calc(edge[i], edge[j])
            if ij_dist < 50:
                graph[i][j] = min(2 + (50 - ij_dist) / 5, ij_dist / 5)
                graph[j][i] = graph[i][j]


            else:
                graph[i][j] = 2 + (ij_dist - 50) / 5
                graph[j][i] = graph[i][j]

dist = [float("inf")] * (n + 2)
dist[0] = 0
heap = [[0, 0]]
while heap:
    now, cur_dist = heappop(heap)
    for next, next_dist in enumerate(graph[now]):
        next_total_dist = cur_dist + next_dist

        if next_total_dist < dist[next]:
            dist[next] = next_total_dist
            heappush(heap, [next, next_total_dist])
print(dist[-1])
