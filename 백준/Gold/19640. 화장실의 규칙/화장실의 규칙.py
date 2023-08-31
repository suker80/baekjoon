from collections import deque
from heapq import *

n, m, k = map(int, input().split())
line = [deque() for _ in range(m)]
line_heap = []
for i in range(n):
    d, h = map(int, input().split())

    line[i % m].append([-d, -h, i % m, k == i])
for i in range(m):
    if line[i]:
        heappush(line_heap, line[i][0])

answer = 0
while line_heap:
    d, h, idx, is_deca = heappop(line_heap)

    if is_deca:
        print(answer)
        break
    answer += 1
    line[idx].popleft()
    if line[idx]:
        heappush(line_heap,line[idx][0])

