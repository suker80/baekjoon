n, m = map(int, input().split())

direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]

graph = [list(map(int, input().split())) for _ in range(n)]

from collections import deque

visit = [[[0] * n for _ in range(n)] for _ in range(2)]

queue = deque([[0, 0, 1, 0, 0]])  # y,x, can_build,time

while queue:
    y, x, can_build, time, cnt = queue.popleft()

    if y == n - 1 and x == n - 1:
        print(time)
        break

    for dy, dx in direction:
        ny, nx = dy + y, dx + x

        if 0 <= ny < n and 0 <= nx < n and visit[can_build][ny][nx] == 0:
            if graph[ny][nx] and (time + 1) % graph[ny][nx] == 0:
                if graph[ny][nx] > 1 and cnt > 0:
                    continue
                temp_cnt = 1 if graph[ny][nx] > 1 else 0
                queue.append([ny, nx, can_build, time + 1, temp_cnt])
                visit[can_build][ny][nx] = 1
            elif graph[ny][nx] and (time + 1) % graph[ny][nx] != 0:
                queue.append([y, x, can_build, time + 1, cnt])
            elif graph[ny][nx] == 0 and can_build:

                if (time + 1) % m != 0:
                    queue.append([y, x, can_build, time + 1, cnt])

                else:
                    if (1 <= ny < n - 1 and graph[ny - 1][nx] and graph[ny + 1][nx]) or (
                            1 <= nx < n - 1 and graph[ny][nx - 1] and graph[ny][nx + 1]):
                        queue.append([ny, nx, 0, time + 1, 1])
                        visit[0][ny][nx] = 1
                    elif (ny == n - 1 and nx == 0) or (nx == n - 1 and ny == 0):
                        queue.append([ny, nx, 0, time + 1, 1])
                        visit[0][ny][nx] = 1
