from heapq import *

for _ in range(int(input())):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for i in range(d):
        a, b, t = map(int, input().split())
        graph[b].append([a, t])

    queue = []
    queue.append([0, c])
    count = 0
    answer = 0
    visit = [False] * (n + 1)
    while queue:
        current, node = heappop(queue)
        if not visit[node]:
            answer = max(current, answer)
            count += 1

        else:
            continue
        visit[node] = True

        for next, next_second in graph[node]:
            if not visit[next]:
                heappush(queue, [next_second + current, next])
    print(count, answer)
