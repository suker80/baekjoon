t = int(input())
from collections import deque
for _ in range(t):

    n = int(input())

    arr = list(map(int,input().split()))
    m = int(input())
    degree = [0] * n

    graph = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i+1,n):

            a,b = arr[i],arr[j]

            graph[b-1][a-1] = 1
            degree[b-1] += 1

    rank = []

    for i in range(m):
        a,b = map(int,input().split())
        if graph[a-1][b-1]:
            graph[b-1][a-1] =1
            graph[a-1][b-1] = 0
            degree[b-1] += 1
            degree[a-1] -= 1
        else:
            graph[b-1][a-1] = 0
            graph[a-1][b-1] = 1
            degree[b-1] -= 1
            degree[a-1] += 1

    queue = deque()
    for i in range(n):

        if degree[i] == 0:
            queue.append(i)
    visit = [0] * n
    answer = []
    while queue:
        cur = queue.popleft()
        answer.append(cur+1)
        visit[cur] = 1
        for i in range(n):

            if graph[i][cur]:
                graph[i][cur] = 0
                degree[i] -= 1

            if degree[i] == 0 and visit[i] == 0 :
                queue.append(i)
    if len(answer) == n:
        print(*answer)
    elif len(answer) != n:
        print('IMPOSSIBLE')


