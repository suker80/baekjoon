n, m = map(int, input().split())
from itertools import permutations

answer = []
for p in permutations(list(range(1, n + 1)), m):
    print(*p)
