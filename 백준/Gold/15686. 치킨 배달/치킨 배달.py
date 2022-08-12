n , m  = map(int,input().split())

city_map = [list(map(int,input().split())) for _ in range(n)]



home = []
chicken = []

for i in range(n):
    for j in range(n):
        if city_map[i][j] == 1:
            home.append((i,j))
        elif city_map[i][j] == 2:
            chicken.append((i,j))

from itertools import combinations

dist = float('inf')

for comb in combinations(chicken,m):
    result = 0 
    
    for h in home:
        min_dist = float('inf')
        for c in comb:
            min_dist = min(min_dist, abs(h[0] - c[0]) + abs(h[1] - c[1]) ) 
        result += min_dist 
    dist = min(dist,result)
    

print(dist)