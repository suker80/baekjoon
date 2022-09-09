import sys
input = sys.stdin.readline
n, l = map(int, input().split())

arr = list(map(int, input().split()))

from collections import deque
queue = deque()



answer=  []
for i in range(n):
    if not queue:
        queue.append([arr[i],i])
        answer.append(queue[0][0])
        continue

    while queue and queue[-1][0] > arr[i]:
        queue.pop()

    while queue and not queue[0][1] >= i - l +1:
        queue.popleft()

    queue.append([arr[i],i])
    answer.append(queue[0][0])
print(' '.join(map(str,answer)))




