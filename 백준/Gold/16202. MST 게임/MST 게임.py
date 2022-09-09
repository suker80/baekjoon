from collections import deque

n, m, k = map(int, input().split())


def union(a, b):
    p_a, p_b = find(a), find(b)
    if p_a < p_b:
        parent[p_b] = p_a
    else:
        parent[p_a] = p_b


def find(v):
    if parent[v] == v:
        return v
    else:
        parent[v] = find(parent[v])
    return parent[v]


edge = []
for i in range(m):
    a, b = map(int, input().split())
    edge.append([a, b, i + 1])

edge.sort(key=lambda x: x[2])

edge = deque(edge)

answer = [0] * k


def mst():
    cnt = n - 1
    idx = 0
    temp_answer = 0
    while cnt:

        if idx >= len(edge): return 0
        while idx < len(edge):
            a, b, w = edge[idx]
            if find(a) != find(b):
                union(a, b)
                temp_answer += w
                cnt -= 1
                idx += 1
                break
            else:
                idx += 1
    return temp_answer


for i in range(k):
    parent = list(range(n + 1))

    if i != 0:
        a, b, w = edge.popleft()
    answer[i] = mst()
    if not answer[i]: break
print(*answer)
