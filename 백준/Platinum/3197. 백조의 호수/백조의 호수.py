r, c = map(int, input().split())
from collections import deque

graph = [list(map(str, input())) for _ in range(r)]

direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]

queue = []


visit = [[0] * c for _ in range(r)]
swan_visit = [[0] * c for _ in range(r)]
swan = []
for i in range(r):
    for j in range(c):

        if graph[i][j] in ['.','L']:
            for dy, dx in direction:

                ny, nx = i + dy, j + dx

                if 0 <= ny < r and 0 <= nx < c and graph[ny][nx] == 'X' and visit[ny][nx] == 0:
                    queue.append([ny, nx])
                    visit[ny][nx] = 1

        if graph[i][j] == 'L':
            swan.append([i,j])
            graph[i][j] = '.'
def bfs(queue):
    next_queue = deque()

    for y, x in queue:

        for dy, dx in direction:
            ny, nx = dy + y, dx + x

            if 0 <= ny < r and 0 <= nx < c :
                if graph[ny][nx] == 'X' and visit[ny][nx] == 0:
                    next_queue.append([ny,nx])
                    visit[ny][nx] = 1

        graph[y][x] = '.'

    return next_queue

def swan_bfs(y=None, x = None,queue = None):
    if queue is None:
        queue = deque([[y, x]])
    next_swan_queue = deque()
    while queue:

        y, x = queue.popleft()

        if y == y2 and x== x2:
            return next_swan_queue,True

        for dy, dx in direction:

            ny, nx = dy + y, dx + x

            if 0 <= ny < r and 0 <= nx < c:

                if graph[ny][nx] == '.' and swan_visit[ny][nx] == 0:

                    queue.append([ny, nx])
                elif graph[ny][nx] == 'X' and swan_visit[ny][nx] ==0:
                    next_swan_queue.append([ny,nx])
                swan_visit[ny][nx] = 1
    return next_swan_queue,False



day = 1
y1,x1 = swan[0]
y2,x2 = swan[1]

swan_queue = None
while day:

    queue = bfs(queue)
    swan_queue ,flag = swan_bfs(y1,x1,swan_queue)

    if flag:
        print(day)
        break
    day += 1
