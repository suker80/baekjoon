v, e = map(int, input().split())
import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline
graph = [[] for _ in range(v + 1)]
for i in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

answer = [False] * (v + 1)
sequence = [0] * (v + 1)
visit = [False] * (v + 1)

counter = 0


def dfs(root, is_root, parent):
    global counter
    visit[root] = True
    counter += 1
    sequence[root] = counter

    min_seq = sequence[root]
    min_child_seq = sequence[root]
    child = 0
    for next_v in graph[root]:
        if sequence[next_v]:
            min_seq = min(min_seq, sequence[next_v])
        else:
            child += 1
            min_child_seq = dfs(next_v, False, root)
            if not is_root and min_child_seq >= sequence[root]:
                answer[root] = True
            min_seq = min(min_seq, min_child_seq)
    if is_root and child >= 2:
        answer[root] = True
    return min_seq


for i in range(1, v + 1):
    if not visit[i]:
        dfs(i, True, i)
answer = [i for i, v in enumerate(answer) if v == True]
print(len(answer))
print(*sorted(answer))
