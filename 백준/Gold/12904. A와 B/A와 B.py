s = input()
t = input()

for i in range(len(t) - len(s)):
    if t[-1] == 'A':
        t = t[:-1]
    elif t[-1] == 'B':
        t = t[-2::-1]
print(int(s == t))
