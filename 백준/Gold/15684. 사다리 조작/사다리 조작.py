from collections import defaultdict

n, m, h = map(int, input().split())
line = []
graph = [[0] * (n + 1) for _ in range(h + 2)]
answer = float('inf')
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[a][b + 1] = - 1


def line_calc(i):
    y, x = 1, i

    while y <= h:
        if graph[y][x] == 0:
            y += 1
            continue
        else:
            x += graph[y][x]
            y += 1
            continue
    if i == x:
        return True
    else:
        return False


def move(count):
    global answer
    for i in range(1, n + 1):
        calc = line_calc(i)

        if not calc:
            return False

    answer = min(answer, count)


def solve(count, y, x):
    if count > 3:
        return
    move(count)
    for i in range(y, h + 1):
        for j in range(1, n):

            if graph[i][j] == 0 and graph[i][j + 1] == 0:
                graph[i][j] = 1
                graph[i][j + 1] = -1
                solve(count + 1, i,1)
                graph[i][j] = 0
                graph[i][j + 1] = 0


solve(0, 1, 1)
print(answer) if answer != float("inf") else print(-1)
