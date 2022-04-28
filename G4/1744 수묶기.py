n = int(input())

arr = [int(input()) for _ in range(n)]
arr.sort(reverse=True)
answer = 0
mid = n
for i in range(n):
    if arr[i] < 1:
        mid = i
        break

pos = arr[:mid]
neg = arr[mid:]

for i in range(1, len(pos), 2):
    answer += max(pos[i] * pos[i - 1], pos[i] + pos[i - 1])

if len(pos) % 2:
    answer += pos[-1]
neg.sort()
for i in range(1, len(neg), 2):
    answer += max(neg[i] * neg[i - 1], neg[i] + neg[i - 1])
if len(neg) % 2:
    answer += neg[-1]
print(answer)