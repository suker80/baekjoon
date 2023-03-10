from collections import deque

n = int(input())

arr = [int(input()) for _ in range(n)]

arr.sort()
negative = []
positive = []
isZero = False
answer = 0
for num in arr:
    if num < 0:
        negative.append(num)
    elif num == 0:
        isZero = True
    else:
        positive.append(num)
negative.sort(reverse=True)
while negative:
    if len(negative) == 1:
        if not isZero:
            answer += negative.pop()
        break

    answer += negative.pop() * negative.pop()
while positive:
    if len(positive) == 1:
        answer += positive.pop()
        break

    pop1 = positive.pop()
    pop2 = positive.pop()
    if pop1 * pop2 > pop1 + pop2:
        answer += pop1*pop2
    else:
        answer += pop1+pop2
print(answer)


