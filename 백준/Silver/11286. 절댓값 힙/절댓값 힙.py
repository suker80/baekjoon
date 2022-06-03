import sys
input = sys.stdin.readline
n = int(input())
from heapq import *

posHeap = []
negHeap = []

answer = []
for i in range(n):
    x = int(input())
    if x > 0:
        heappush(posHeap, x)
    elif x < 0:
        heappush(negHeap, abs(x))
    else:
        if not posHeap and not negHeap:
            answer.append(0)
        elif posHeap and not negHeap:
            answer.append(heappop(posHeap))
        elif negHeap and not posHeap:
            answer.append(-heappop(negHeap))
        else:
            if negHeap[0] <= posHeap[0]:
                answer.append(-heappop(negHeap))
            else:
                answer.append(heappop(posHeap))
print('\n'.join(map(str,answer)))