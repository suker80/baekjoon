n = int(input())
import bisect

arr = list(map(int, input().split()))

arr.sort()
answer = [arr[0], arr[-1]]
min_val = abs(sum(answer))

left, right = 0, n - 1
while right > left:

    s = arr[right] + arr[left]
    if min_val > abs(s):
        answer = [arr[left], arr[right]]
        min_val = abs(s)
    if s > 0:

        right -= 1
    else :

        left += 1
print(*answer)
