import sys
from collections import defaultdict

size = int(input())
n, m = map(int, input().split())

a = [int(input()) for i in range(n)]
b = [int(input()) for i in range(m)]

pre_a = defaultdict(int)
pre_b = defaultdict(int)
a_table = [[0] * n for _ in range(n)]
b_table = [[0] * m for _ in range(m)]

sum_a = sum(a)
sum_b = sum(b)
answer = 0

for i in range(n):
    for j in range(i, n):
        if i == j:
            a_table[i][j] = a[i]
        else:
            a_table[i][j] = a_table[i][j - 1] + a[j]

        pre_a[a_table[i][j]] += 1

        if i > 0 and j < n - 1:
            pre_a[sum_a - a_table[i][j]] += 1

for i in range(m):
    for j in range(i, m):
        if i == j:
            b_table[i][j] = b[i]
        else:
            b_table[i][j] = b_table[i][j - 1] + b[j]

        pre_b[b_table[i][j]] += 1

        if i > 0 and j < m - 1:
            pre_b[sum_b - b_table[i][j]] += 1

for key ,val in sorted(pre_a.items()):
    if key > size:
        break
    answer += pre_a[key] * pre_b[size-key]
answer += pre_a[size]
answer += pre_b[size]
print(answer)
