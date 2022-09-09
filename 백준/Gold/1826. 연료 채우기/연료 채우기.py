from heapq import *

n = int(input())

arr = []

for i in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])
l, p = map(int, input().split())

heap = []
arr.sort(key=lambda x: (x[0], -x[1]))
cur = p
idx = 0
ans = 0
while cur < l:
    while idx < n and arr[idx][0] <= cur:
        heappush(heap, -arr[idx][1])
        idx += 1
    if not heap:
        break

    cur -= heap[0]
    ans += 1
    heappop(heap)

print(ans) if cur >= l else print(-1)
