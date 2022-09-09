n,k = map(int,input().split())

arr = list(map(int,input().split()))

temp = set()

answer = 0

import heapq
for i in range(k):
    if len(temp) < n:
        temp.add(arr[i])
    if arr[i] not in temp:
        heap = []
        for t in temp:
            for j in range(i+1,k):
                if arr[j] == t:
                    heapq.heappush(heap,[-j,t])
                    break
            else:
                heapq.heappush(heap,[-10000,t])
        answer += 1
        dist, v = heapq.heappop(heap)

        temp.discard(v)
        temp.add(arr[i])

print(answer)
