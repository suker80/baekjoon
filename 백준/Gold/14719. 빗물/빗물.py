h, w = map(int, input().split())
left, right = 0, 0
arr = list(map(int, input().split()))
stack = []
answer = 0
for i in range(len(arr)):
    if not stack and arr[i] > left:
        left = arr[i]
        continue
    if arr[i] < left:
        stack.append(arr[i])
        continue
    if stack and left <= arr[i]:
        while stack:
            answer += left - stack.pop()
        left = arr[i]
if stack:
    right = stack[-1]
while stack:
    if stack[-1] < right:
        answer += right - stack.pop()
    else:
        right = stack.pop()

print(answer)