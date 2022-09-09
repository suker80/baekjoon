from collections import defaultdict, Counter

n = int(input())
arr = list(map(int, input().split()))

counter = Counter(arr)
dic = defaultdict(int)
answer = 0
for i in range(n):
    for j in range(i + 1, n):
        a, b = arr[i], arr[j]

        if a and b:
            dic[a + b] = 1
        elif not a and b:
            if counter[b] > 1:
                dic[a + b] = 1
        elif a and not b:
            if counter[a] > 1:
                dic[a + b] = 1
        else:
            if counter[a] > 2:
                dic[a] = 1
for i in range(n):
    if dic[arr[i]]:
        answer += 1

print(answer)
