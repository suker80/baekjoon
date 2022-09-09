n = int(input())

norm_dic = {"R": 0, "G": 1, "B": 2}
abnorm_dic = {"R": 0, "G": 0, "B": 1}

norm_pic = []
abnorm_pic = []
for i in range(n):
    p = input()
    norm_p = [norm_dic[i] for i in p]
    norm_pic.append(norm_p)

    abnorm_p = [abnorm_dic[i] for i in p]
    abnorm_pic.append(abnorm_p)

pic = [norm_pic, abnorm_pic]

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

from collections import deque

def bfs(start, visit, graph):
    queue = deque([start])
    y, x = start
    color = graph[y][x]
    while queue:
        y, x = queue.popleft()
        visit[y][x] = 1

        for dy, dx in direction:
            ny, nx = y + dy, x + dx

            if 0 <= ny < n and 0 <= nx < n and graph[ny][nx] == color and visit[ny][nx] == 0:
                queue.append((ny, nx))
                visit[ny][nx] = 1
    return visit


t = 2
result = []
for p in pic:
    visit = [[0] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0:
                visit = bfs((i, j), visit, p)
                count += 1
    result.append(count)
print(*result)