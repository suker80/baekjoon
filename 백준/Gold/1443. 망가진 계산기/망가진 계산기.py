d, p = map(int, input().split())
from itertools import *
max_val = 10 ** (d)
import sys
answer = 1
if 1 << p >= max_val:
    print(-1)
    sys.exit()


def calc(comb):
    res = 1
    for i in comb:
        res *= i
    return res
for comb in combinations_with_replacement(range(2,10),p):

    res = calc(comb)
    if res < max_val:
        answer = max(answer,res)
print(answer)


