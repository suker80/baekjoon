from heapq import *

n = int(input())
graph = []
for i in range(n):
    arr = list(map(int, input().split()))
    graph.append(arr)

heap = []
answer = 0
visit = [False] * n
heap.append([0, 0])
while heap:
    c, e = heappop(heap)
    if visit[e]:
        continue
    visit[e] = True
    answer += c
    for i in range(n):
        if i != e and not visit[i]:
            heappush(heap, [graph[e][i], i])
print(answer)
