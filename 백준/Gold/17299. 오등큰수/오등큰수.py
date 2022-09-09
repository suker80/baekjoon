from collections import Counter
n = int(input())

answer = 0

arr = list(map(int,input().split()))
answer = [-1] * n
counter= Counter(arr)
stack = []
stack.append(0)
for i in range(1,n):
    while stack and counter[arr[stack[-1]]] < counter[arr[i]]:
        answer[stack[-1]] = arr[i]
        stack.pop()



    stack.append(i)
print(*answer)