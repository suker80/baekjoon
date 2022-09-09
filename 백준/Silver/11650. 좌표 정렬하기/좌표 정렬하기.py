n = int(input())

point = [list(map(int,input().split())) for _ in range(n)]

for _ in sorted(point):
    print(*_)