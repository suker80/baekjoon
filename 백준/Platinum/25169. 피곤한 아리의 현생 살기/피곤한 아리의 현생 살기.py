n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

k = 0
total_k = sum([i[0] for i in arr])
answer = 0


def calc(job, k):
    r, s = job
    total_sum = 0
    for i in range(r):
        total_sum += s * (i + 1) * (1 + (k + i) * 0.1)
    return total_sum


for i in range(n - 1, -1, -1):
    for j in range(i):
        left = arr[i]
        right = arr[j]
        if calc(right, 0) + calc(left, right[0]) > calc(left, 0) + calc(right, left[0]):
            arr[i], arr[j] = arr[j], arr[i]
answer = 0
for i in range(n):
    answer += calc(arr[i], k)
    k += arr[i][0]
print(int(answer))