from collections import deque

n = int(input())
arr = list(map(int, input().split()))
if n == 1:
    if arr[0] % 3 == 0:

        print("YES")
        exit()
    else:
        print("NO")
        exit()

if sum(arr) % 3 != 0:
    print("NO")
    exit()

flag = True
idx = 0

one_count = 0
not_one_count = 0
for i in range(n):
    if arr[i] == 1:
        one_count += 1
    else:
        not_one_count += arr[i] // 2
        if arr[i] % 2:
            one_count += 1
if not_one_count < one_count:
    print("NO")
    exit()
else:
    print("YES")
    exit()
