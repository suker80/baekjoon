t = int(input())
import sys
sys.setrecursionlimit(112345)
for _ in range(t):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    rev_graph = [[] for _ in range(n + 1)]
    visit = [False] * (n + 1)
    rev_visit = [False] * (n + 1)
    degree = [0] * (n + 1)
    isSCC = [False] * (n + 1)
    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        rev_graph[b].append(a)
    
    stack = []
    answer = 0
    
    
    def dfs(node):
        visit[node] = True
    
        for next in graph[node]:
            if not visit[next]:
                visit[next] = True
                dfs(next)
        stack.append(node)
    
    
    def rev_dfs(node, parent):
        rev_visit[node] = parent
        for next in rev_graph[node]:
            if not rev_visit[next]:
                visit[next] = parent
                rev_dfs(next, parent)
    
    
    dfs_count = 0
    for i in range(1, n + 1):
        if not visit[i]:
            dfs_count += 1
            dfs(i)
    
    while stack:
        top = stack.pop()
        if not rev_visit[top]:
            rev_dfs(top, top)
            isSCC[top] = True
        else:
            answer += 1
    
    start = []
    
    for i in range(1, n + 1):
        for next in graph[i]:
            if rev_visit[i] != rev_visit[next]:
                degree[rev_visit[next]] += 1
    print(len([i for i in range(1, n + 1) if not degree[i] and isSCC[i]]))
