n,m = map(int,input().split())
a_i = list(map(int,input().split()))

import heapq

heap = []
for a in a_i:
    heapq.heappush(heap,a)
count = 1

while count <= m:
    x = heapq.heappop(heap)
    y = heapq.heappop(heap)
    result = x+y

    heapq.heappush(heap,result)
    heapq.heappush(heap,result)
    count +=1

print(sum(heap))