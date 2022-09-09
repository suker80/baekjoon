import sys
from heapq import *

n = int(input())
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort(key=lambda x: (x[1], -x[0]))
days = 1
answer = 0
heap = []
heap_len = 0
for i in range(n):
    cup, deadline = arr[i]

    if heap_len < deadline:
        heappush(heap, cup)
        heap_len += 1
    elif heap[0] < cup:
        heappop(heap)
        heappush(heap, cup)
print(sum(heap))
