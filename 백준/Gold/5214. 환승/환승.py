n,k,m = map(int,input().split())
from itertools import combinations
from collections import deque
import sys

input = sys.stdin.readline

visit = [0] * (n+1)

graph = [[] for _ in range(n+1)]
hyper = []
for i in range(m):

    lst = list(map(int,input().split()))

    hyper.append(lst)

    for j in lst:
        graph[j].append(i)




queue = deque([[1,1]])

while queue:
    node ,count= queue.popleft()
    visit[node] = 1

    if node == n:
        print(count)
        break

    for h in graph[node]:

        for v in hyper[h]:

            if visit[v] == 0:
                queue.append([v,count+1])
                visit[v] = 1

else:
    print(-1)
