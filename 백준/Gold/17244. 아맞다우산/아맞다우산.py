m, n = map(int, input().split())

graph = [list(map(str, input())) for _ in range(n)]


from collections import deque

direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
queue = deque()
b= 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'S':
            queue.append([i, j, 0, 0])
            graph[i][j] = '.'
        if graph[i][j] == 'E':
            e_pos = [i, j]
        if graph[i][j] == 'X':
            graph[i][j] = 1<<b
            b += 1
visit = [[[0] * m for _ in range(n)] for _ in range(1<<b)]

while queue:

    y, x, count, bit = queue.popleft()
    visit[bit][y][x] = 1
    if [y, x] == e_pos and bit == (1<<b )- 1 :
        print(count)
        break

    for dy, dx in direction:
        ny, nx = dy + y, dx + x

        if 0 <= ny < n and 0 <= nx < m and visit[bit][ny][nx] == 0 and graph[ny][nx] != '#':

            if graph[ny][nx] in [1,2,4,8,16] and visit[bit|graph[ny][nx]][ny][nx] == 0 :
                queue.append([ny,nx,count+1,bit | graph[ny][nx]])
                visit[bit|graph[ny][nx]][ny][nx] = 1
            elif graph[ny][nx] == '.' or graph[ny][nx] == 'E' and visit[bit][ny][nx] == 0:
                queue.append([ny,nx,count+1,bit])
                visit[bit][ny][nx] = 1

