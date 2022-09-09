n, k = map(int, input().split())

arr = [int(input()) for _ in range(n)]

max_val = max(arr)

for i in range(n):
    for j in range(i+1,n):

        a = str(arr[i]) + str(arr[j])
        b= str(arr[j]) + str(arr[i])

        if int(a) > int(b):
            continue
        else:
            arr[j],arr[i] = arr[i] , arr[j]

answer = ''

repeat = k - n + 1
max_idx = arr.index(max_val)
for i in range(n):
    if i == max_idx:
        answer += str(arr[i]) * repeat
    else:
        answer += str(arr[i])

print(answer)