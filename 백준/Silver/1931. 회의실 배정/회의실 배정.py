n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort(key=lambda x: (x[1], x[0]))

answer = 1
time = arr[0][1]
for i in range(1, n):
    if arr[i][0] < time:
        continue
    else:
        answer += 1
        time = arr[i][1]
print(answer)
