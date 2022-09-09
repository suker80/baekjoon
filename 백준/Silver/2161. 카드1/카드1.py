n = int(input())

from collections import deque

arr = deque(list(range(1, n + 1)))
answer = []
while len(arr) > 1:
    print(arr.popleft(),end = ' ')
    arr.append(arr.popleft())
print(*arr)
