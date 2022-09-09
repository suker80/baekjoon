import heapq
import sys

n = int(input())
heap = []

for _ in range(n):

    op = int(sys.stdin.readline())
    if op:
        heapq.heappush(heap, op)
    else:
        if len(heap):
            print(heapq.heappop(heap))
        else:
            print(0)