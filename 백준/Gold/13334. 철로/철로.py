n = int(input())
import sys
input = sys.stdin.readline

from heapq import heappop,heappush
from heapq import heappushpop
arr = []
for i in range(n):
    a,b = map(int,input().split())
    if a> b:
        b,a = a,b
    arr.append([a,b])
s = int(input())
arr.sort(key=lambda x: (x[1],x[0]))
answer = 0
count = 0
heap = []
for i in range(n):
    if not heap and abs(arr[i][1] - arr[i][0]) <= s :
        heappush(heap,arr[i])
        count += 1
        left, right = arr[i][1] - s , arr[i][1]
        continue

    if abs(arr[i][1] - arr[i][0]) > s :
        continue

    left, right = arr[i][1] - s , arr[i][1]
    heappush(heap,arr[i])
    count += 1
    while heap[0][0] < left:
        heappop(heap)
        count -= 1
    answer = max(answer,count)


print(answer)