n,m= map(int,input().split())

graph= [[] for  _ in range(n)]

for i in range(n):
    lst = list(map(int,input().split()))

    graph[i] = lst[1:]

d = [-1] * (m+1)
def dfs(node):

    if visit[node] : return

    visit[node] = True


    for next_node in graph[node]:

        if d[next_node] == -1 or dfs(d[next_node]):
            d[next_node] = node
            return True

    return False

answer=  0
for i in range(n):
    visit = [False] * (n+1)

    if dfs(i):
        answer +=1
print(answer)