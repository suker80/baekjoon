n = int(input())
m = int(input())
from collections import deque
graph = [[float('inf')] * n for _ in range(n)]

for i in range(m):
    a, b, = map(int, input().split())
    graph[a - 1][b - 1] = 1
    graph[b - 1][a - 1] = 1

for k in range(n):
    graph[k][k] = 0
    for i in range(n):
        for j in range(n):
            graph[i][j]  = min(graph[i][j],graph[i][k]+ graph[k][j] )

component = []
comp = 0
visit = [False] * n
def bfs(i):
    visit[i] = True
    queue = deque([i])
    com = [i]
    while queue:
        v = queue.popleft()

        for i in range(n):
            if graph[v][i] != float('inf') and visit[i] == False:
                com.append(i)
                queue.append(i)
                visit[i] = True
    return com
for i in range(n):
    if visit[i] == False:
        comp= bfs(i)
        component.append(comp)

answer=  []
for group in component:
    mval = []
    m = 0
    for v in group:
        m = 0
        for w in group:
            m = max(graph[v][w],m)
        mval.append([m , v+1])
    mval.sort(key= lambda x: x[0])
    answer.append(mval[0][1])
answer.sort()
print(len(component))
print(*answer ,sep = '\n')


