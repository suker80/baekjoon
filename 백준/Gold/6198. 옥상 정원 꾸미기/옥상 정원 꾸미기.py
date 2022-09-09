n = int(input())
answer = 0

stack = []
for i in range(n):
    cur = int(input())
    if not stack:
        stack.append([cur, i])
        continue

    while stack and stack[-1][0] <= cur:
        prev, idx = stack.pop()
        answer += (i - idx) - 1
    stack.append([cur, i])

stack.pop()
while stack:
    prev ,idx = stack.pop()
    answer += (i - idx)
print(answer)