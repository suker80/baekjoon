import sys
from collections import Counter

string = input()

counter = Counter(string)

a = counter['A']
b = counter['B']
c = counter['C']


def solve(a, b, c, current, before, before2):
    if not a and not b and not c:
        print(current)
        sys.exit()
    if dp[a][b][c][before][before2]: return

    dp[a][b][c][before][before2] = True
    if a:
        solve(a - 1, b, c, current + 'A', before2, 0)

    if b:
        if before2 != 1:
            solve(a, b - 1, c, current + "B", before2, 1)
    if c:
        if before != 2 and before2 != 2:
            solve(a, b, c - 1, current + "C", before2, 2)


dp = [[[[ [False] * 3 for _ in range(3)] for _ in range(51)] for _ in range(51)] for _ in range(51)]
solve(a, b, c, "", -1, -1)
print(-1)
