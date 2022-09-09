import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline

v, e = map(int, input().split())

graph = [[] for _ in range(v + 1)]

for i in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)

count = 1
d = [0] * (v + 1)
stack = []
finished = [False] * (v + 1)

answer = []


def dfs(start):
    global count
    d[start] = count
    count += 1
    stack.append(start)

    parent = d[start]
    for next in graph[start]:

        if not d[next]:
            parent = min(parent, dfs(next))

        elif not finished[next]:
            parent = min(parent, d[next])

    if parent == d[start]:
        temp = []

        while stack:

            top = stack.pop()
            temp.append(top)

            finished[top] = True

            if start == top:
                break

        temp.sort()
        answer.append(temp)

    return parent


for i in range(1, v + 1):

    if d[i] == 0:
        dfs(i)
answer = sorted(answer, key=lambda x: x[0])
print(len(answer))
for arr in answer:
    print(*arr, -1)
