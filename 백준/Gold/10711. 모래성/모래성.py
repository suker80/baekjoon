import sys

input = sys.stdin.readline
n, m = map(int, input().rstrip().split())

graph = [list(map(str, input())) for _ in range(n)]

from collections import deque

direction = [[1, 0], [1, -1], [1, 1], [0, 1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
queue = deque()
visit = [[False] * m for _ in range(n)]


def check(i, j):
    cnt = 0
    for dy, dx in direction:
        ny, nx = i + dy, j + dx
        if 0 <= ny < n and 0 <= nx < m:
            if graph[ny][nx] == '.': cnt += 1
    if graph[i][j] <= cnt:
        return True
    else:
        return False


for i in range(n):
    for j in range(m):

        if ord('1') <= ord(graph[i][j]) <= ord('9'):
            graph[i][j] = int(graph[i][j])
            if check(i, j):
                queue.append([i, j])
                visit[i][j] = True
days = 0
next_queue = deque()

while True:
    if not queue: break
    days += 1
    while queue:

        y, x = queue.popleft()
        graph[y][x] = '.'

        for dy, dx in direction:
            ny, nx = y + dy, x + dx

            if 0 <= ny < n and 0 <= nx < m and ord('1') <= ord(str(graph[ny][nx])) <= ord('8') and not visit[ny][nx]:
                if check(ny, nx):
                    next_queue.append([ny, nx])
                    visit[ny][nx] = True

    queue = next_queue
    next_queue = deque()

print(days)
