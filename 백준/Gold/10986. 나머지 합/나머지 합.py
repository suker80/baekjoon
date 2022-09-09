n, m = map(int, input().split())

arr = list(map(int, input().split()))
prefix = [0] * (n + 1)

cnt = [0] * (m)
s = 0
answer = 0
for i in range(n):
    s += arr[i]

    if not s%m : answer += 1
    cnt[s % m] += 1
for i in range(0,m):
    answer += (cnt[i] * (cnt[i] -1)) //2
print(answer)
