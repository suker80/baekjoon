n = int(input())
from datetime import date
from heapq import *

start, end = date(2022, 3, 1).toordinal(), date(2022, 11, 30).toordinal()
flowers = []
heap = []
answer = 0
for i in range(n):
    a, b, c, d = map(int, input().split())
    flowers.append([date(2022, a, b).toordinal(), date(2022, c, d).toordinal()])

flowers.sort(key=lambda x: (x[0], -x[1]))

idx = 0
while idx < n and flowers[idx][0] <= start:
    heappush(heap, -flowers[idx][1])
    idx += 1

while heap and idx < n:
    pop = -heappop(heap)
    heap.clear()
    answer += 1
    if pop > end:
        print(answer)
        exit()
    while idx < n and flowers[idx][0] <= pop:
        heappush(heap, -flowers[idx][1])
        idx += 1

if heap:
    last = -heappop(heap)
    print(answer + 1) if last > end else print(0)
else:
    print(0)
