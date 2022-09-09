n,m = input().split()
from itertools import combinations
from collections import deque
m = int(m)

max_val = 0
queue = deque([n])

for i in range(m):
    next_q = set()
    while queue:
        now = queue.popleft()
        for i,j in combinations(range(len(n)),2):
            next_num = now[:i] + now[j] + now[i+1:j] + now[i] + now[j+1:]
            if next_num[0] == '0':
                continue
            next_q.add(next_num)
    queue = deque(next_q)
    if not queue:
        break
if queue:
    queue = list(map(int,queue))
    print(max(queue))
else:
    print(-1)