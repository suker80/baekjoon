from collections import defaultdict

n, m, p = map(int, input().split())
name_lst = input().split()

dic = {}
for name in name_lst:
    dic[name] = [[-1, False] for _ in range(n + 1)]

leaderboard = [[] for _ in range(n + 1)]
p_lst = []
for i in range(p):
    num, t, name, isSolve = input().split()
    t = t.split(":")
    t = int(t[0]) * 60 + int(t[1])
    p_lst.append([int(num), t, name, isSolve == "solve"])

p_lst.sort(key=lambda x: x[1])

for num, t, name, isSolve in p_lst:
    cur = dic[name][num]
    if isSolve:
        if cur[0] == -1:
            cur[1] = True
        elif not cur[1]:
            cur[1] = True
            leaderboard[num].append([t - cur[0],name])
    else:
        if cur[0] == -1 and not cur[1]:
            cur[0] = t

point = defaultdict(int)
for num in range(1, n + 1):
    leaderboard[num].sort()
    for idx, score in enumerate(leaderboard[num]):
        point[score[1]] += 1 + idx

for name in name_lst:
    for num in range(1, n + 1):

        isSolve = dic[name][num][1]

        t = dic[name][num][0]
        if not isSolve:
            if t == -1:
                point[name] += m + 1
            else:
                point[name] += m
        elif isSolve:
            if t == -1:
                point[name] += m + 1

for name, p in sorted(list(point.items()), key=lambda x: (x[1], x[0])):
    print(name)
