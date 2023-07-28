from collections import *


def solution(maps):
    answer = -1
    direction = ((1, 0), (-1, 0), (0, 1), (0, -1))

    n = len(maps)
    m = len(maps[0])
    visit = [[[0] * m for _ in range(n)] for _ in range(2)]
    queue = deque()
    for i in range(n):
        maps[i] = list(maps[i])
        for j in range(m):
            if maps[i][j] == 'S':
                queue.append([0, 0, i, j])

    while queue:
        count, is_lever, y, x = queue.popleft()
        visit[is_lever][y][x] = 1

        for dy, dx in direction:
            ny, nx = dy + y, dx + x
            if 0 <= ny < n and 0 <= nx < m and not visit[is_lever][ny][nx] and maps[ny][nx] != 'X':
                visit[is_lever][ny][nx] = 1
                if is_lever == 0 and maps[ny][nx] == 'L':
                    queue.append([count + 1, 1, ny, nx])
                elif maps[ny][nx] =='E' and is_lever:
                    return count+1
                else:
                    queue.append([count + 1, is_lever, ny, nx])
                


    return answer