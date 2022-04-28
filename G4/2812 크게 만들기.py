from collections import Counter, deque

n, k = map(int, input().split())
arr = list(map(int, input()))
cnt = 0
idx = 0
stack = []
for i, v in enumerate(arr):

    while k and stack and stack[-1][0] < v:
        _, idx = stack.pop()
        arr[idx] = ''
        k -= 1

    stack.append([v, i])

while k:
    _,idx = stack.pop()
    arr[idx] = ''
    k -= 1
print(''.join(map(str, arr)))
