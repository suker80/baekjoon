from collections import deque

n, q = map(int, input().split())
mod = 1_000_000_007
arr = ['0'] + input().split()
graph = [[] for _ in range(n + 1)]
answer = []


def bfs(node, end):
    queue = deque()
    queue.append([node, arr[node]])

    while queue:
        here, here_dist = queue.popleft()
        visit[here] = True
        if here == end:
            return here_dist
        for next in graph[here]:
            if not visit[next]:
                visit[next] = True
                queue.append([next, str(int(here_dist + arr[next]) % mod)])


for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(q):
    visit = [False] * (n + 1)
    a, b = map(int, input().split())

    answer.append(bfs(a, b))

print('\n'.join(answer))
