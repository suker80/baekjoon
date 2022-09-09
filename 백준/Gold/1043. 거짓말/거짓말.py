n, m = map(int, input().split())

know = list(map(int, input().split()))

know_truth = [False] * (n+1)
for i in know[1:]:
    know_truth[i] = True

party = [list(map(int, input().split()))[1:] for _ in range(m)]
parent = list(range(n + 1))


def find(v):
    if parent[v] == v:
        return parent[v]
    else:
        parent[v] = find(parent[v])
        return parent[v]


def union(a, b):
    pa, pb = find(a), find(b)

    if pa != pb:
        if know_truth[pa]:
            parent[pb] = pa
        else:
            parent[pa] = pb


for p in party:
    for i in range(len(p) - 1):
        union(p[i], p[i + 1])

answer = 0
for p in party:
    for i in p:
        if know_truth[find(i)]:
            break
    else:
        answer+=1
print(answer)
