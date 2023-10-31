n = int(input())
from heapq import *
heap = []

arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort()
answer = 0
for i in range(n):
    if heap and heap[0] <= arr[i][0]:
        heappop(heap)
    heappush(heap,arr[i][1])
    answer = max(answer,len(heap))

print(answer)