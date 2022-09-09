from bisect import bisect_left

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
idx = bisect_left(arr, 0)

pos = [0] + arr[idx:]
neg = [0] + arr[:idx]
neg = sorted(map(abs, neg))
pos_cost = 0
neg_cost = 0

for i in range(len(pos) - 1, -1, -m):
    pos_cost += (pos[i] * 2)
for i in range(len(neg) - 1, -1, -m):
    neg_cost += (neg[i] * 2)
answer = (pos_cost + neg_cost) - max(pos[-1], neg[-1])
print(answer)
