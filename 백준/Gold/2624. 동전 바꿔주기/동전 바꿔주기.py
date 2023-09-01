from collections import defaultdict

t = int(input())
k = int(input())
coins = [list(map(int, input().split())) for _ in range(k)]

cost = defaultdict(int)
cost[0] = 1
for coin, num in coins:

    for i in range(t, -1, -1):
        for j in range(1, num + 1):
            if i - (j * coin) >= 0:
                cost[i] += cost[i - (j * coin)]
print(cost[t])
