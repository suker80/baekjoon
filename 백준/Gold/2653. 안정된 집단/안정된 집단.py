n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

visit = [False] * n

answer = 0
answer_list = []

for i in range(n):
    for j in range(n):
        if graph[i][j] != graph[j][i]:
            print(0)
            exit(0)


def dfs(node):
    visit[node] = True

    for next in range(n):
        if graph[node][next] == 0 and not visit[next]:
            temp.append(next + 1)
            visit[next] = True
            dfs(next)


for i in range(n):
    if not visit[i]:
        visit[i] = True
        answer += 1
        temp = [i + 1]
        dfs(i)
        answer_list.append(sorted(temp))

for lst in answer_list:
    
    if len(lst) < 2:
        print(0)
        exit(0)
print(answer)
answer_list.sort(key=lambda x: x[0])
for i in range(answer):
    print(*answer_list[i])
