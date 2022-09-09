from sys import stdin

n, k = map(int, stdin.readline().rstrip().split())
students = [0] * n
data = [0] * 21
count = 0

for rank in range(n):
    name = len(stdin.readline().rstrip())
    students[rank] = name
    if rank > k:
        data[students[rank - k - 1]] -= 1
    count += data[name]
    data[name] += 1

print(count)