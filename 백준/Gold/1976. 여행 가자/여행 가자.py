n = int(input())
m = int(input())
from collections import deque
graph = [list(map(int,input().split())) for _ in range(n)]


plan = list(map(int,input().split()))

parent = [False] * n

def bfs(start):

    queue = deque([start])
    max_val = start
    lst = [start]
    while queue:
        node = queue.popleft()
        for i in range(n):
            if graph[node][i] and not parent[i]:
                queue.append(i)
                lst.append(i)
                max_val = max(i,max_val)
                parent[i] = max_val

    for l in lst:
        parent[l] = max_val
output = 'YES'

for i in range(n):
    if not parent[i]:
        bfs(i)

for i in range(m-1):
    if parent[plan[i]-1] == parent[plan[i+1]-1]:
        continue
    else:
        output = 'NO'
        break
print(output)




