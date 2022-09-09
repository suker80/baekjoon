import re

n, k = map(int, input().split())
rep = '[acint]'
alpha = 'abcdefghijklmnopqrstuvwxyz'
alpha = re.sub(rep, '', alpha)

dic = {}
for idx, char in enumerate(alpha):
    dic[char] = idx
words = [0] * n
for i in range(n):
    string = input()
    bit = 0

    string = re.sub(rep, '', string)
    string = list(set(string))

    for char in string:
        bit |= 1 << dic[char]
    words[i] = bit

answer = 0


def solve(idx, count, bit):
    global answer
    if 21 - count + 1 < idx:
        return

    if count == 0:
        ans = 0
        for i in range(n):
            if words[i] & bit == words[i]:
                ans += 1
        answer = max(answer, ans)
        return
    for i in range(idx, 21):
        solve(i+1, count - 1, bit | 1 << i)


solve(0, k - 5, 0)
print(answer)
