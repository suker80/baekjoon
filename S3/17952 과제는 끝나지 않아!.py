import sys

input = sys.stdin.readline
n = int(input())

answer = 0
stack = []

for i in range(1, n + 1):
    lst = list(map(int, input().split()))
    if lst[0]:
        stack.append([lst[1], lst[2]])

    if stack:
        stack[-1][-1] -= 1
        if stack[-1][-1] == 0:
            pop = stack.pop()
            answer += pop[0]


print(answer)