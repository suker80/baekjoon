n = int(input())

answer = float('inf')
import sys

def isGood(String):
    for i in range(1, len(String) // 2 + 1):
        for j in range(len(String)  - i):
            left = String[j:j + i ]
            right = String[j + i:j + i + i]
            if left == right:
                return False

    return True


def solve(current):
    global answer
    if not isGood(current):
        return
    elif len(current) == n:
        print(current)
        sys.exit()
        return

    for i in ['1', '2', '3']:
        if current and current[-1] == i:
            continue
        solve(current + i)


solve('')
print(answer)
