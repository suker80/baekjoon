from bisect import *

n = int(input())
arr = list(map(int, input().split()))

answer = 0
lisArray = [arr[0]]

for i in range(1, n):
    current = arr[i]

    if current > lisArray[-1]:
        lisArray.append(current)
    else:
        left = bisect_left(lisArray,current)
        lisArray[left] = current
        answer +=1
print(answer)

