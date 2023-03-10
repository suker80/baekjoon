n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

people = 0
for i in range(n):
    people += arr[i][1]

arr.sort()
people_sum = 0
for i in range(n):
    people_sum += arr[i][1]
    if people_sum >= people / 2:
        print(arr[i][0])
        break
