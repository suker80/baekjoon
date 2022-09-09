import sys

input = sys.stdin.readline
r, c = map(int, input().split())

graph = [list(map(str, input().rstrip())) for _ in range(r)]
command = list(map(int, input().rstrip()))
direction = [[0, 0], [1, -1], [1, 0], [1, 1], [0, -1], [0, 0], [0, 1], [-1, -1], [-1, 0], [-1, 1]]

aduino = []
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'I':
            start_y, start_x = i, j
        elif graph[i][j] == 'R':
            aduino.append([i, j])
count = 0


def calc_dist(a, start):
    return abs(a[0] - start[0]) + abs(a[1] - start[1])


for k, op in enumerate(command):
    dy, dx = direction[op]
    graph[start_y][start_x] = '.'
    start_y, start_x = start_y + dy, start_x + dx
    if graph[start_y][start_x] == 'R':
        print('kraj {}'.format(k + 1))
        sys.exit()

    graph[start_y][start_x] = 'I'
    boom = []
    next_aduino = set()

    for a in aduino:
        i, j = a
        graph[i][j] = '.'

    for a in aduino:
        i, j = a
        dist = calc_dist([i, j], [start_y, start_x])
        for dy, dx in direction:
            temp_y, temp_x = i + dy, j + dx
            temp_dist = calc_dist([temp_y, temp_x], [start_y, start_x])
            if temp_dist < dist:
                dist = temp_dist
                ny, nx = temp_y, temp_x
        if graph[ny][nx] == 'I':
            print('kraj {}'.format(k + 1))
            sys.exit()

        else:
            if graph[ny][nx] == 'R':
                boom.append([ny, nx])
                continue
            graph[ny][nx] = 'R'
            next_aduino.add((ny,nx))
    aduino = []

    for by, bx in boom:
        graph[by][bx] = '.'
    aduino = next_aduino - set(map(tuple,boom))


for _ in graph:
    print(''.join(_))
