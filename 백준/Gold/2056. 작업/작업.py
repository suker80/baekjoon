n = int(input())
from collections import deque
graph= [ [] for _ in range(n+1)]

val = [0] * (n+1)

degree=  {}

queue = deque()
for i in range(1,n+1):

    lst = list(map(int,input().split()))

    val[i] = lst[0]
    if lst[1] == 0:
        queue.append(i)
    degree[i] = lst[1]

    for j in lst[2:]:
        graph[j].append(i)

answer= val[:]
while queue :

    current = queue.popleft()

    for i in graph[current]:
        degree[i] -= 1
        if degree[i] == 0 :
            queue.append(i)
        answer[i] = max(answer[i] , answer[current] + val[i])

print(max(answer))