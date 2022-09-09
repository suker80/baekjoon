n, m = map(int, input().split())
from collections import deque

graph = [list(input()) for _ in range(n)]
direction = [[0, 1], [0, -1], [1, 0], [-1, 0], [0, 0]]
visit = [[[[0] * m for _ in range(n)] for _ in range(4)] for _ in range(4)]

target = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'S':
            s_y, s_x = [i, j]
            graph[i][j] = '.'
        elif graph[i][j] == 'C':
            target.append([i, j])


def bfs(s_y, s_x):
    queue = deque()
    queue.appendleft([s_y, s_x, 0, 4, 0])

    while queue:
        y, x, found, dir, time = queue.popleft()
        if found == 3:
            return time

        for cur_dir in range(4):
            if cur_dir == dir:
                continue
            dy, dx = direction[cur_dir]

            ny, nx = y + dy, x + dx

            if 0 <= ny < n and 0 <= nx < m and visit[cur_dir][found][ny][nx] == 0:

                if graph[ny][nx] == '#':
                    continue
                elif graph[ny][nx] == '.':
                    visit[cur_dir][found][ny][nx] = 1
                    queue.append([ny, nx, found, cur_dir, time + 1])
                elif graph[ny][nx] == 'C':

                    bit = target.index([ny, nx])

                    visit[cur_dir][found | (bit + 1)][ny][nx] = 1
                    # graph[ny][nx] = '.'
                    queue.append([ny, nx, found | (bit + 1), cur_dir, time + 1])


answer = bfs(s_y, s_x)
print(answer) if answer else print(-1)
