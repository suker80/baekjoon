from itertools import permutations

a, b = input().split()
answer = 0
for per in permutations(a, len(a)):
    if per[0] == '0':
        continue
    i = int(''.join(per))
    if i < int(b):
        answer = max(answer,i)

if answer:
    print(answer)
else:
    print(-1)
