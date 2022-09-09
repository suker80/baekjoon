n = int(input())

arr = list(map(int, input().split()))

answer = 0


def solve(cnt):
    global answer
    for i, v in enumerate(arr):
        if i == 0 or i == len(arr) - 1:
            continue
        else:

            temp = cnt + (arr[i - 1] * arr[i + 1])
            answer = max(temp, answer)
            arr.pop(i)
            solve(temp)
            arr.insert(i, v)


for i in range(n):
    if i == 0 or i == len(arr) - 1:
        continue
    else:
        solve(0)
print(answer)
