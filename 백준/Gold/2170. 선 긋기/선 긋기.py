n = int(input())
import sys
input = sys.stdin.readline
lines = [list(map(int, input().split())) for _ in range(n)]

lines.sort(key=lambda x: (x[0], x[1]))

left = lines[0][0]
right = lines[0][1]
answer = 0
for i in range(1, n):
    if lines[i][0] > right:
        answer += abs(right - left)
        left = lines[i][0]
        right = lines[i][1]
    else:
        left = min(left, lines[i][0])
        right = max(right, lines[i][1])
answer += abs(right - left)
print(answer)
