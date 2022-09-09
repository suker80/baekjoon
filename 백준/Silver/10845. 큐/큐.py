from collections import deque

queue = deque()
n = int(input())
import sys
for _ in range(n):
    command = sys.stdin.readline().split()
    
    c= command[0]
    
    if c== 'push':
        queue.append(command[1])
    elif c == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif c=='size':
        print(len(queue))
    elif c== 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif c == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif c == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)