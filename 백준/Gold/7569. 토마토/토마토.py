import sys
n, m, h = map(int, input().split())

box = [[list(map(int, input().split())) for i in range(m)] for _ in range(h)]
if 0 not in [j for d in box for i in d for j in i]:
    print(0)
    sys.exit()
from collections import deque

direction = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, -1), (0, 0, 1)]
queue = deque([])
for z in range(h):
    for x in range(n):
        for y in range(m):
            if box[z][y][x] == 1:
                queue.append((z,y,x))

while queue:
    z,y,x = queue.popleft()

    for dy, dx, dz in direction:
        ny, nx, nz = y + dy, x + dx, z + dz
        if 0 <= ny < m and 0 <= nx < n and 0 <= nz < h and box[nz][ny][nx] == 0:
            queue.append((nz,ny, nx))
            box[nz][ny][nx] = box[z][y][x] + 1

print(-1) if 0 in [j for d in box for i in d for j in i] else print(max([j for d in box for i in d for j in i]) -1 )