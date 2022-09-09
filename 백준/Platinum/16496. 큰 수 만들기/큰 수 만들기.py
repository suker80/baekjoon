n = int(input())
arr = input().split()

for i in range(n - 1, -1, -1):
    for j in range(i):
        if int(arr[j] + arr[j + 1]) < int(arr[j + 1] + arr[j]):
            arr[j + 1], arr[j] = arr[j], arr[j + 1]

print(int(''.join(arr)))
