k,n = map(int,input().split())
from heapq import heappop,heappush,heapify
prime = list(map(int,input().split()))

heapify(prime)
heap = prime[:]

count = 0



for i in range(n):
    top = heappop(heap)
    for p in prime:

        next = top * p
        if next > 2**31 :
            break
        heappush(heap,next)
        if top % p == 0 :
            break






print(top)