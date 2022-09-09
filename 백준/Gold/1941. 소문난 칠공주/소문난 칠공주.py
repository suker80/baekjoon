graph = [input() for _ in range(5)]
from itertools import combinations
count = 0
from collections import deque
mapping = [0] * 25
s_map = []

direction = [(1,0),(-1,0),(0,1),(0,-1)]
for i in range(25):
    y,x = i//5, i%5
    if graph[y][x] == 'S':
        mapping[i] = 1
        s_map.append(i)
max_s = len(s_map)

def dfs(comb):
    temp_count = 1
    comb = [[i//5,i%5]for i in comb]
    queue = deque([comb.pop()])

    while queue:
        y,x = queue.popleft()

        for dy,dx in direction:
            ny,nx = dy+y,dx+x
            if 0<=ny<5 and 0<=nx<5 and [ny,nx] in comb:
                comb.remove([ny,nx])
                queue.append([ny,nx])
                temp_count +=1
    if temp_count == 7:
        return True
    else :
        return False




all_map = range(25)
for my_comb in combinations(range(25),7):
    if len(set(s_map).intersection(set(my_comb))) >=4:
        if dfs(my_comb):
            count +=1
        else:
            continue




print(count)