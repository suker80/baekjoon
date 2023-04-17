from heapq import heappush, heappop

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort()
heap = []
heappush(heap,[arr[0][1],arr[0][0]])
answer = 0
for i in range(1, n):
    start, end = arr[i]
    heappush(heap, [end,start])
    while heap and heap[0][0] <= start:
        heappop(heap)
    answer = max(len(heap), answer)
print(answer)
