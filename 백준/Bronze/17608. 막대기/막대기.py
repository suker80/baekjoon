n = int(input())

arr = [int(input()) for _ in range(n)]

stack = []
arr.reverse()

stack.append(arr[0])
answer = 1
for i in range(1,n):

    if arr[i] > stack[-1]:
        stack.append(arr[i])
        answer += 1
    else:
        continue

print(answer)