n = int(input())
import sys
input = sys.stdin.readline
homework = [list(map(int,input().split())) for _ in range(n)]


homework.sort(key=lambda x:(-x[1] ,x[0]))
answer= 0
plan = [0] * 1002
for h in homework:

    day,weight = h
    for j in range(day,0,-1):
        if plan[j] == 0:
            plan[j] += weight
            break
print(sum(plan))
