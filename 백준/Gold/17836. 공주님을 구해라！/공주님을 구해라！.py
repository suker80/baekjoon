n, m, t = map(int, input().split())

direction = [[1, 0], [-1, 0], [0, -1], [0, 1]]
from collections import deque

graph = [list(map(int, input().split())) for _ in range(n)]

visit = [[0] * m for _ in range(n)]
queue = deque([[0, 0, 0]])


def solve():
    result = float('inf')

    while queue:
        y, x, count = queue.popleft()

        if count > t:
            if result <= t:
                print(result)
            else:
                print("Fail")
            return
        if y == n - 1 and x == m - 1:
            print(min(count, result))
            return
        for dy, dx in direction:
            ny, nx = dy + y, dx + x

            if 0 <= ny < n and 0 <= nx < m:

                if not visit[ny][nx]:
                    if graph[ny][nx] == 2:
                        visit[ny][nx] = 1
                        result = count + 1 + (n - ny - 1) + (m - nx - 1)
                    elif graph[ny][nx] == 0:
                        visit[ny][nx] = 1
                        queue.append([ny, nx, count + 1])

    print(result) if result <= t else print("Fail")


solve()
