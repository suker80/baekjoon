import sys

n = int(input())
m = int(input())

city = [[float('inf')] * n for _ in range(n)]

for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    city[a-1][b-1] = min(city[a-1][b-1], c)

for k in range(n):
    city[k][k] = 0
    for j in range(n):
        for i in range(n):

            city[i][j] = min(city[i][j],city[i][k]+city[k][j])

for i in range(n):
    for j in range(n):
        if city[i][j] == float('inf'):
            city[i][j] = 0
for c in city:
    print(*c)