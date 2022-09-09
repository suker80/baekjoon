import sys
import heapq

input = sys.stdin.readline
n = int(input())
lessons = [list(map(int, input().split())) for _ in range(n)]

lessons.sort()

heap = []
for lesson in lessons:
    if heap and heap[0] <= lesson[0]:
        heapq.heappop(heap)
    heapq.heappush(heap, lesson[1])


print(len(heap))