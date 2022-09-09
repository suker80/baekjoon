n= int(input())
import sys
input= sys.stdin.readline
from heapq import heappop,heappush

left_heap , right_heap = [],[]
for i in range(n):
    x = int(input())
    if i == 0 :
        heappush(left_heap,x)
        print(x)
    elif i==1:
        l = heappop(left_heap)
        if l<x:
            heappush(left_heap,-l)
            heappush(right_heap,x)
            print(l)
        else:
            heappush(left_heap,-x)
            heappush(right_heap,l)
            print(x)
    else:
        if len(left_heap) <= len(right_heap):
            if right_heap[0] > x:
                heappush(left_heap,-x)

            else:
                r = heappop(right_heap)
                heappush(left_heap,-r)
                heappush(right_heap,x)
        elif len(left_heap) > len(right_heap):

            if -left_heap[0] < x:
                heappush(right_heap,x)
            else:
                l = -heappop(left_heap)
                heappush(left_heap,-x)
                heappush(right_heap,l)
        print(-left_heap[0])






