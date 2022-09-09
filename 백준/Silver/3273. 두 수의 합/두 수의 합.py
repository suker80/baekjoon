n = int(input())

arr = list(map(int, input().split()))

target = int(input())

arr.sort()

left, right = 0, n - 1
answer = 0
while right > left:

    temp = arr[left] + arr[right]

    if temp == target:
        answer += 1
        left += 1
    elif temp > target:
        right -= 1
    elif temp < target:
        left += 1
print(answer)