r, c, n = map(int, input().split())

graph = [list(map(str, input())) for _ in range(r)]
direction = [[1, 0], [-1, 0], [0, -1], [0, 1]]
time = [[-1] * c for _ in range(r)]

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'O':
            time[i][j] = 0

for t in range(n):

    bomb = []

    for i in range(r):
        for j in range(c):

            if graph[i][j] == '.' and time[i][j] == -1 and t != 0:
                graph[i][j] = 'O'
                time[i][j] = 0
            elif graph[i][j] == 'O':

                time[i][j] +=1

                if time[i][j] == 3 :
                    bomb.append([i,j])
    for y,x in bomb:
        graph[y][x] = '.'
        time[y][x] = -1
        for dy,dx in direction:
            ny,nx = dy+y,dx+x
            if 0<=ny<r and 0<=nx < c:
                graph[ny][nx] ='.'
                time[ny][nx] = -1

for _ in graph:
    print(''.join(_))