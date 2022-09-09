t = int(input())
from collections import deque,defaultdict

direction = [[1,0],[-1,0],[0,1],[0,-1]]
for _ in range(t):
    n,m = map(int,input().split())

    graph = [ ['.'] * (m+2) for _ in range(n+2)]


    for i in range(n):
        lst = input()
        for j,e in enumerate(lst):
            graph[i+1][j+1] = e

    n,m= n+2,m+2
    key_dict = defaultdict(int)
    has_key = input()
    for k in has_key:
        key_dict[k] = 1
    answer =0

    visit = [[0] * m for _ in range(n)]
    queue = deque([[0,0]])
    dq = defaultdict(lambda :deque())
    while queue:
        y,x = queue.popleft()
        visit[y][x] = 1
        for dy ,dx in direction:
            ny,nx = dy+y,dx+x

            if 0<=ny < n and 0<=nx<m:
                if graph[ny][nx] == '*':
                    continue
                if visit[ny][nx] == 1:
                    continue

                if ord('A') <= ord(graph[ny][nx]) <= ord('Z'):

                    if key_dict[graph[ny][nx].lower()]:
                        graph[ny][nx] = '.'
                        visit[ny][nx] = 1
                        queue.append([ny, nx])
                    else:
                        dq[graph[ny][nx].lower()].append([ny,nx])

                elif ord('a') <= ord(graph[ny][nx]) <= ord('z'):
                    key = graph[ny][nx]
                    key_dict[key] = 1
                    graph[ny][nx] = '.'

                    while dq[key]:
                        queue.append(dq[key].popleft())
                    queue.append([ny,nx])

                elif graph[ny][nx] == '.' and visit[ny][nx] ==0 :
                    visit[ny][nx] = 1
                    queue.append([ny,nx])

                elif graph[ny][nx] == '$':

                    answer += 1
                    graph[ny][nx] = '.'
                    queue.append([ny,nx])
    print(answer)








