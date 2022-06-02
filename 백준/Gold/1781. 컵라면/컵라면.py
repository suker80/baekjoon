import sys
from heapq import *

n = int(input())
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort(key=lambda x: (x[0], -x[1]))
days = 1
answer = 0
heap = []
heap_len = 0
for i in range(n):
    deadline, cup = arr[i]

    if heap_len < deadline:
        heappush(heap, cup)
        heap_len += 1
    elif heap[0] < cup:
        heappop(heap)
        heappush(heap, cup)
print(sum(heap))

