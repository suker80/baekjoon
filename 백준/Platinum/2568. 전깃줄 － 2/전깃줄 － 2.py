n = int(input())
from collections import deque
import bisect

lines = [list(map(int, input().split())) for _ in range(n)]

temp_lines =sorted(lines,key=lambda x:x[0])
dp = deque([temp_lines[0][1]])

set_answer = set([l[0] for l in temp_lines])

count = 0
answer= {temp_lines[0][0]:1}
for i in range(1, n):
    if temp_lines[i][1] > dp[-1]:
        dp.append(temp_lines[i][1])
        answer[temp_lines[i][0]] = bisect.bisect_left(dp,temp_lines[i][1]) + 1
    else:
        idx = bisect.bisect_left(dp, temp_lines[i][1])
        answer[temp_lines[i][0]] = idx + 1
        dp[idx] = temp_lines[i][1]

lis_l= len(dp)
temp = []
for key,value in sorted(answer.items(),reverse=True):
    if answer[key] == lis_l:
        temp.append(key)
        lis_l -= 1
    if lis_l <= 0:
        break
answer = list(set(answer) - set(temp))
print(len(answer))
print(*answer , sep='\n')