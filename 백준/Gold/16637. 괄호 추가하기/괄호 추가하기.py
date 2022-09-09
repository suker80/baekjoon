n = int(input())
import sys

sys.setrecursionlimit(10000)
arr = list(map(str, input()))
arr = [int(i) if 48 <= ord(i) <= 57 else i for i in arr]


def p(a, b): return a + b


def mult(a, b): return a * b


def mi(a, b): return a - b


func = {'+': p, '-': mi, '*': mult}

dp = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(i, n):

        if i == j:
            dp[i][j] = arr[i]
        elif j % 2 == 1:
            dp[i][j] = dp[i][j - 1]
        else:
            dp[i][j] = func[arr[j - 1]](dp[i][j - 1], arr[j])
        if i % 2 == 1: dp[i][j] = dp[i - 1][j]

answer = -float('inf')


def solve(idx, s, left=None, right=None):
    global answer
    if idx > n:
        if answer < s:
            answer = max(answer, s)
        return

    if idx > 0 and left is None:
        s = func[arr[idx - 1]](s, arr[idx])
    else:
        s = s

    if left is None and right is None:
        if idx < 0:

            solve(idx + 2, arr[0], left, right)
        else:
            solve(idx + 2, s, left, right)
        if n - idx > 4:
            solve(idx + 2, s, idx + 2, right)
    ## 괄호가 닫혔을떄
    if left is not None and right is not None:
        if left <= 0:
            solve(idx + 2, s + dp[left][right], None, None)
            if n - idx > 4:
                solve(idx + 2, s + dp[left][right], idx + 2, None)
        else:
            solve(idx + 2, func[arr[left - 1]](s, dp[left][right]), None, None)
            if n - idx > 4:
                solve(idx + 2, func[arr[left - 1]](s, dp[left][right]), idx + 2, None)

    ## 왼쪽만 열렸을 때
    if left is not None and right is None:
        solve(idx + 2, s, left, idx + 2)


solve(-2, 0)
print(answer)
