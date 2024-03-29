import sys
from heapq import heappush, heappop
input = sys.stdin.readline
n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]

arr.sort()
heap = []
heappush(heap,arr[0][1])
answer = 0
for i in range(1, n):
    start, end = arr[i]
    heappush(heap, end)
    while heap and heap[0] <= start:
        heappop(heap)
    answer = max(len(heap), answer)
print(answer)
