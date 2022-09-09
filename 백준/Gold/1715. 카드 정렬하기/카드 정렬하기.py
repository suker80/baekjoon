import sys

n = int(input())
from heapq import *
input = sys.stdin.readline
heap = [int(input()) for _ in range(n)]

heapify(heap)
answer = 0
while heap:

    if heap:
        first = heappop(heap)
    if heap:
        second = heappop(heap)
        heappush(heap, first + second)
        answer += (first + second)
    else:
        print(answer)
        break