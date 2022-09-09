n, m, k = map(int, input().split())
from collections import deque
import sys

input = sys.stdin.readline
ground = [list(map(int, input().split())) for _ in range(n)]
temp_ground = [[5]*n for _ in range(n)]

tree = [[deque() * (n+1) for _ in range(n+1)] for _ in range(n+1)]
direction = [-1, 0, 1]
for i in range(m):
    y,x,z = map(int,input().split())
    tree[y][x].append(z)
dead_tree = deque()

def spring():
    global tree
    global temp_ground

    for i in range(1,n+1):
        for j in range(1, n + 1):
            for a in range(len(tree[i][j])):
                if temp_ground[i-1][j-1] >= tree[i][j][a]:
                    temp_ground[i-1][j-1] -= tree[i][j][a]
                    tree[i][j][a] += 1
                else:
                    for b in range(a,len(tree[i][j])):
                        age = tree[i][j].pop()
                        dead_tree.append([i,j,age])
                    break




    while dead_tree:
        y,x, z = dead_tree.popleft()
        temp_ground[y - 1][x - 1] += z // 2






    for y in range(1,n+1):
        for x in range(1,n+1):
            for age in tree[y][x]:
                if age % 5 == 0:
                    for dy in direction:
                        for dx in direction:
                            ny, nx = y + dy, x + dx
                            if dy==0 and dx==0: continue
                            if 1<= ny <= n and 1 <= nx <= n:
                                tree[ny][nx].appendleft(1)


    for i in range(n):
        for j in range(n):
            temp_ground[i][j] += ground[i][j]

for i in range(k):
    spring()


cnt = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):

        cnt += len(tree[i][j])
print(cnt)