n,m = map(int,input().split())
from itertools import combinations

comb = [[1] * 101 for _ in range(101)]

for i in range(1,101):
    for j in range(1,i):
        comb[i][j] = comb[i-1][j-1] + comb[i-1][j]
print(comb[n][m])