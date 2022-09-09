n = int(input())

arr = list(map(int, input().split()))
arr_sort = sorted(arr, reverse=True)

c = int(input())

while c:
    for i in range(n):
        max_val = max(arr[i:c + 1 + i])
        max_index = arr.index(max_val)

        while c and max_index > i:
            arr[max_index], arr[max_index - 1] = arr[max_index - 1], arr[max_index]
            max_index -= 1
            c -= 1

        if not c: break
    else:
        break

print(*arr)
