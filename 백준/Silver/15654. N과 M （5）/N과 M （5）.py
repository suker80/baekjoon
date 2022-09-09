n,m = map(int,input().split())
from itertools import permutations
arr = list(map(int,input().split()))
arr.sort()
for c in permutations(arr,m):
    print(*c)
