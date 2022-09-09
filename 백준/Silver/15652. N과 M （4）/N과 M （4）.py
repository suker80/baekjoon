n,m = map(int,input().split())
from itertools import combinations_with_replacement

for c in combinations_with_replacement(range(1,n+1),m):
    print(*c)
