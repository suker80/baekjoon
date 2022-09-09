n, m, k = map(int, input().split())
from collections import deque
import sys
input = sys.stdin.readline
visit = [[[0] * m for _ in range(n)] for _ in range(k + 1)]

graph = [list(map(int, list(map(str, input().rstrip())))) for _ in range(n)]

direction = [[1, 0], [-1, 0], [0, -1], [0, 1]]


def bfs():
    queue = deque([[0, 0, k, 1]])
    next_queue = deque()
    visit = [[[0] * m for _ in range(n)] for _ in range(k + 1)]

    visit[k][0][0] = 1
    day = 1
    while True:
        while queue:
            y, x, wall,count = queue.popleft()

            if y == n - 1 and x == m - 1:
                print(count)
                sys.exit()

            for dy, dx in direction:
                ny, nx = dy + y, dx + x

                if 0 <= ny < n and 0 <= nx < m:

                    if visit[wall][ny][nx] == 0:

                        if graph[ny][nx] == 0:
                            next_queue.append([ny, nx,wall,count+1])
                            visit[wall][ny][nx] = 1
                        elif graph[ny][nx] == 1:

                            if day == 1 and wall > 0 and visit[wall-1][ny][nx] == 0 :

                                visit[wall-1][ny][nx] = 1

                                next_queue.append([ny, nx, wall - 1,count+1])
                            elif day == 0:
                                next_queue.append([y,x,wall,count+1])



        else:
            queue = next_queue
            next_queue = deque()
            day = 1 - day

            if not queue:
                print(-1)
                break
bfs()