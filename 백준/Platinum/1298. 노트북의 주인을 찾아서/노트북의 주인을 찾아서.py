n,m = map(int,input().split())
import sys

input = sys.stdin.readline

matching = [-1] * (n+1)

graph = [[] for _ in range(n+1)]


def dfs(node):

    if visit[node] == 1: return

    visit[node] = 1


    for note in graph[node]:

        if matching[note] == -1 or dfs(matching[note])  :
            matching[note] = node
            return True
    return False


for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)




answer= 0
for i in range(1,n+1):
    visit = [0] *(n+1)

    if dfs(i) :
        answer += 1

print(answer)