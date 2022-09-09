import sys
from heapq import heappop,heappush
input = sys.stdin.readline

from collections import deque
n,k = map(int,input().split())
jewel = []
for i in range(n):
    weight,price = map(int,input().split())
    jewel.append([weight,price])

jewel.sort(key=lambda x:x[0])
jewel = deque(jewel)

bag= [int(input()) for i in range(k)]
bag.sort()
answer=  0
heap = []
for i in range(k):
    b = bag[i]

    while jewel and jewel[0][0] <= b:
        w,p = jewel.popleft()
        heappush(heap,-p)
    if heap:
        answer -= heappop(heap)
print(answer)






