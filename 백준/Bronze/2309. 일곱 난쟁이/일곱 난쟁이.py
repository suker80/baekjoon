n = 9
arr = [int(input()) for _ in range(n)]

arr.sort()

s = sum(arr)

def solve():
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == s - 100:
                for _ in range(n):
                    if _ == i or _ == j:
                        continue
                    else:
                        print(arr[_])
                return
solve()