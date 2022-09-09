n = int(input())

pos = [list(map(int, input().split())) for _ in range(n)]
dist = [[0] * n for _ in range(n)]
min_avg = float('inf')
for i in range(n):
    cur_max = -float('inf')
    for j in range(n):
        if i== j : continue
        d = ((pos[i][0] - pos[j][0]) ** 2 + (pos[i][1] - pos[j][1]) ** 2) ** 0.5
        if d > cur_max:
            cur_max = d

    if min_avg > cur_max:
        min_avg = cur_max
        answer = i
print(*pos[answer])
