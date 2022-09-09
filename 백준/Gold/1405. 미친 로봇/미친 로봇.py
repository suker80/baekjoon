n, right, left, down, up = map(int, input().split())

right, left, down, up = right / 100, left / 100, down / 100, up / 100

graph = [[False] * (2 * n + 1) for _ in range(2 * n + 1)]

start = n, n

direction = [[0, 1], [0, -1], [-1, 0], [1, 0]]

prob = [right, left, up, down]

answer = 0


def solve(move, y, x, cur):
    global answer
    if move >= n:
        answer += cur
        return

    graph[y][x] = True
    for i, d in enumerate(direction):
        if prob[i] == 0: continue

        dy, dx = d
        ny, nx = dy + y, dx + x
        if graph[ny][nx]: continue
        graph[ny][nx] = True
        solve(move + 1, ny, nx, cur * prob[i])
        graph[ny][nx] = False


solve(0, n, n, 1)
print(answer)
