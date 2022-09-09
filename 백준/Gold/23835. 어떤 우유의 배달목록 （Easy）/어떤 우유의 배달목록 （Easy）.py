n = int(input())

graph = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

q = int(input())

answer = [0] * n


def dfs(node, end, cnt=0):
    if node == end:
        answer[end] += cnt
        return cnt
    visit[node] = True
    for next in graph[node]:

        if not visit[next]:
            if dfs(next, end, cnt + 1):
                answer[node] += cnt
                return cnt

    return 0


for i in range(q):
    query = list(map(int, input().split()))
    visit = [False] * n

    if query[0] == 1:
        start, end = query[1] - 1, query[2] - 1
        dfs(start, end)
    else:
        print(answer[query[1] - 1])
