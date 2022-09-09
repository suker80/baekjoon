import sys
input = sys.stdin.readline
from collections import deque
n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

degree = [0] * (n+1)
base = [{} for _ in range(n+1)]
rev_graph = [[] for _ in range(n+1)]
for i in range(m):
    x,y,k = map(int,input().split())

    graph[y].append([x,k])
    rev_graph[x].append([y,k])
    degree[x] += 1
answer = []
queue = deque([])
for i in range(1,n+1):
    if not degree[i]:
        queue.append(i)
        answer.append(i)



while queue:
    cur = queue.popleft()

    for v,w in graph[cur]:
        degree[v] -= 1


        if not base[v].get(cur):
            base[v][cur] = w
        if cur not in answer:
            for key,value in base[cur].items():

                if not base[v].get(key):
                    base[v][key] = w*value
                else:
                    base[v][key] += value * w
        if degree[v] == 0:
            queue.append(v)

for a in answer:
    print(a,base[n][a])





