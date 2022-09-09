n,m = map(int,input().split())

from collections import defaultdict,deque
import sys
sys.stdin.readline
indegree = [0] *(n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    seq = list(map(int,input().split()))

    for i in range(1,len(seq) -1 ):
        a,b = seq[i],seq[i+1]
        graph[a].append(b)

        indegree[b] +=1
queue = deque()

answer = []
for i in range(1,n+1):
    if not indegree[i]:
        queue.append(i)
while queue:
    cur = queue.popleft()
    answer.append(cur)
    for v in graph[cur]:
        indegree[v] -= 1

        if indegree[v] == 0:
            queue.append(v)


if len(answer) != n:
    print(0)
else:
    print(*answer,sep='\n')