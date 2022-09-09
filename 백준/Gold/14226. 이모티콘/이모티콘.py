n = int(input())

from collections import deque

visit = [[False] * 5000 for _ in range(20000)]

queue = deque([[1, 0, 0]])
while queue:
    s, count, clip = queue.popleft()

    if s == n:
        print(count)
        break

    ns = s + clip
    if ns > 0 and not visit[clip][ns]:
        queue.append([ns, count + 1, clip])
        visit[clip][ns] = True

    if clip != s and s<=1000 and clip <= 1000:
        queue.append([s, count + 1, s])
    ns = s - 1
    if ns > 0 and not visit[clip][ns]:
        queue.append([ns, count + 1, clip])
        visit[clip][ns] = True
