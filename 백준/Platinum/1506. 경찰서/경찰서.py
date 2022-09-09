n = int(input())
import sys
sys.setrecursionlimit(100000)
input =sys.stdin.readline
cost = list(map(int, input().split()))
graph = [list(map(int,list(input().rstrip()))) for _ in range(n)]
rev_graph = [[] for _ in range(n)]
stack = []

for i in range(n):
    graph[i] = [idx for idx,flag in enumerate(graph[i]) if flag == 1]

for i in range(n):
    for j in graph[i]:
        rev_graph[j].append(i)

visit = [False] * n
def dfs(node):
    visit[node] = True
    for next in graph[node]:
        if not visit[next]:
            dfs(next)
    stack.append(node)

for i in range(n):
    if not visit[i]:
        dfs(i)

rev_visit = [False] * n
scc = []

def rev_dfs(node,min_cost):

    rev_visit[node] = True
    min_cost = min(min_cost,cost[node])
    for next in rev_graph[node]:
        if not rev_visit[next]:
            min_cost = min(rev_dfs(next,min_cost), min_cost)

    return min_cost
answer =0
while stack:
    top = stack.pop()
    if rev_visit[top]:
        continue
    else:
        min_cost = rev_dfs(top,cost[top])
        answer += min_cost
print(answer)