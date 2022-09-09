import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

t = int(input())


def dfs(node):
    visit[node] = True
    stack.append(node)

    if not visit[arr[node]]:
        dfs(arr[node])
    elif arr[node] != node and visit[arr[node]] and not cant_cycle[arr[node]] and not project[arr[node]]:

        while stack and stack[-1] != arr[node]:
            project[stack.pop()] = True
        project[stack.pop()] = True


for i in range(t):
    n = int(input())
    arr = [0] + list(map(int, input().split()))

    answer = 0

    visit = [False] * (n + 1)
    cant_cycle = [False] * (n + 1)
    project = [False] * (n + 1)
    stack = []
    for i in range(1, n + 1):
        if arr[i] == i:
            visit[i] = True
            project[i] = True

        if not visit[i]:
            dfs(i)
            while stack:
                cant_cycle[stack.pop()] = True

    print(n - sum(project))
