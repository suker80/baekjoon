n = int(input())
graph =[set() for _ in range(n+1)]
weight = [0] * (n+1)
from collections import deque
queue = deque()

for i in range(1,n+1):
    lst = list(map(int,input().split()))
    if len(lst) == 2:
        w = lst[0]
        weight[i] = w
        queue.append(i)
        continue
    else:
        w = lst[0]
        temp = lst[1:-1]
        for v in temp:
            graph[i].add(v)
        weight[i] = w
answer= weight[:]
visit = [False] * (n+1)
while queue:
    current = queue.popleft()
    visit[current] = True
    for i in range(1,n+1):
        if current in graph[i]:
            graph[i].discard(current)
            answer[i] = max(answer[i],answer[current] + weight[i])
            if visit[i] == False and not graph[i]:
                queue.append(i)
                visit[i] =True

print(*answer[1:],sep='\n')
