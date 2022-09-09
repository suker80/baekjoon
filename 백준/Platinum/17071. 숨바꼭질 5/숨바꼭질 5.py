n, k = map(int, input().split())

from collections import deque

queue = deque([n])
next_queue = deque()
time = 0

target = k
visit = [[0] * 500001 for _ in range(2)]
visit[0][n] = 1
while time <= 1001:
    target += time

    if target > 500000:
        print(-1)
        break
    if visit[time % 2][target] != 0:
        print(time)
        break

    while queue:
        cur = queue.popleft()
        next_pos = [cur - 1, cur * 2, cur + 1]

        for next in next_pos:

            if 0 <= next <= 500000 and visit[1 - time % 2][next] == 0:
                next_queue.append(next)
                visit[1 - time % 2][next] = 1

    queue = next_queue
    next_queue = deque()
    time += 1
