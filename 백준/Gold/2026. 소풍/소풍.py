k, n, f = map(int, input().split())
import sys

graph = [[] for _ in range(n + 1)]
friend = [0] * (n + 1)
graph[0] = list(range(1, n + 1))
connect = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(f):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

    connect[a][b] = 1
    connect[b][a] = 1

    friend[a] += 1
    friend[b] += 1

for i in range(n+1):
    graph[i].sort()
visit = [False] * (n + 1)


def solve(cnt, ans, cur):
    if cnt == 0:
        print(*sorted(ans), sep='\n')
        sys.exit()

    for next in graph[cur]:
        if visit[next]: continue

        if k-1 > friend[next]: continue

        for cur_f in ans:
            if not connect[cur_f][next]:
                break
        else:
            visit[next] = True
            solve(cnt - 1, ans + [next], next)
            visit[next] = False


solve(k, [], 0)
print(-1)
