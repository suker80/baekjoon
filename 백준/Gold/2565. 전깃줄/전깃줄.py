n = int(input())

lines = [list(map(int, input().split())) for _ in range(n)]

temp_lines = [l[1] for l in sorted(lines)]
dp = [temp_lines[0]]


import bisect

for i in range(1, n):
    if temp_lines[i] > dp[-1]:
        dp.append(temp_lines[i])
    else:
        idx = bisect.bisect_left(dp, temp_lines[i])
        dp[idx] = temp_lines[i]
print(n - len(dp))

