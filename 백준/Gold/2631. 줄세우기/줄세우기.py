n = int(input())

arr = [int(input()) for _ in range(n)]

dp = [arr[0]]


def lowerBound(arr, key):
    left, right = 0, len(arr) - 1

    while right > left:
        mid = (left + right) // 2

        if arr[mid] < key:
            left = mid + 1
        elif arr[mid] > key:
            right = mid
        elif arr[mid] == key:
            right = mid
    return right


for i in range(1, n):

    if dp[-1] < arr[i]:
        dp.append(arr[i])
    elif dp[-1] > arr[i]:

        idx = lowerBound(dp, arr[i])
        dp[idx] = arr[i]
print(n - len(dp))