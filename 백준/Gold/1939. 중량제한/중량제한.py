n, m = map(int, input().split())
from collections import deque

graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

start, end = map(int, input().split())

left, right = 1, 1_000_000_123


def bfs():
    visit = [False] * (n + 1)
    queue = deque([[start, float('inf')]])
    min_val = float('inf')

    can_visit = False
    while queue:
        cur, weight = queue.popleft()
        if cur == end: return True
        visit[cur] = True
        for next, next_weight in graph[cur]:
            if not visit[next] and next_weight >= mid:
                queue.append([next, min(next_weight, weight)])
                visit[next] = True

    return can_visit


answer = 0
while right > left:

    mid = (left + right) // 2

    flag = bfs()

    if flag:
        left = mid + 1
        answer = max(answer, mid)
    else:
        right = mid

print(answer)
