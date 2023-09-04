n = int(input())
arr = list(map(int, input().split()))

suffix_sum = [0] * n
suffix_sum[0] = arr[0]
answer = 0


def get_suffix_sum_from_to(f, t):
    global suffix_sum
    return suffix_sum[t] - suffix_sum[f] + arr[f]




for i in range(1, n):
    suffix_sum[i] = suffix_sum[i - 1] + arr[i]

middle = 0
for i in range(1, n - 1):
    # 꿀통이 오른쪽
    middle = get_suffix_sum_from_to(i, n - 1) - arr[i] - arr[i]
    left = suffix_sum[n - 1] - arr[0]
    answer = max(answer, middle + left)

    # 꿀통이 가운데
    left = get_suffix_sum_from_to(0, i)
    right = get_suffix_sum_from_to(i, n - 1)
    answer = max(answer, left + right - arr[0] - arr[n - 1])

    # 꿀통이 왼쪽에 있을때
    right = suffix_sum[n - 1] - arr[n - 1]
    middle = get_suffix_sum_from_to(0, i) - arr[i] - arr[i]
    answer = max(answer, right + middle)
print(answer)