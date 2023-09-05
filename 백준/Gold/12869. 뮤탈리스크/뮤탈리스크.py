import itertools
import math
from collections import deque

comb3 = list(itertools.permutations([9, 3, 1], 3))
comb2 = list(itertools.permutations([9, 3], 2))
n = int(input())
scv = list(map(int, input().split()))

if n == 1:
    print(math.ceil(scv[0] / 9))

elif n == 2:
    visit = [[float('inf')] * 61 for _ in range(61)]
    queue = deque()

    queue.append(scv + [0])

    while queue:
        a, b, count = queue.popleft()
        if sum([a, b]) == 0:
            print(count)
            break
        for d_a, d_b in comb2:
            na = max(a - d_a, 0)
            nb = max(b - d_b, 0)

            if visit[na][nb] > count + 1:
                queue.append([na, nb, count + 1])


else:
    visit = [[[float('inf')] * 61 for _ in range(61)] for _ in range(61)]

    queue = deque()

    queue.append(scv + [0])

    while queue:
        a, b, c, count = queue.popleft()
        if sum([a, b, c]) == 0:
            print(count)
            break
        for d_a, d_b, d_c in comb3:

            if not a and d_a == 9:
                continue
            if not b and d_b == 9:
                continue
            if not c and d_c == 9:
                continue

            na = max(a - d_a, 0)
            nb = max(b - d_b, 0)
            nc = max(c - d_c, 0)

            if visit[na][nb][nc] > count + 1:
                visit[na][nb][nc] = count + 1
                queue.append([na, nb, nc, count + 1])
