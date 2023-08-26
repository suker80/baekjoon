import sys

input = sys.stdin.readline
n, m = map(int, input().split())
growth = [list(map(int, input().split())) for _ in range(m)]

arr = [[1] * n for _ in range(n)]

for i in range(m):
    temp = []
    for j, g in enumerate(growth[i]):
        temp += [j] * g
    for j in range(n):
        arr[n - j - 1][0] += temp[j]
        arr[0][j] += temp[n + j - 1]
    arr[0][0] -= temp[n - 1]

for i in range(1, n):
    for j in range(1, n):
        arr[i][j] = max(arr[i - 1][j], arr[i][j - 1], arr[i - 1][j - 1])
for i in range(n):
    print(*arr[i])
