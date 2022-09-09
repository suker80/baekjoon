import sys

input = sys.stdin.readline
n = int(input())
price = list(map(int, input().split()))

graph = [[] for _ in range(n)]

for i in range(n):
    p = int(input())
    for _ in range(p):
        a, cost = map(int, input().split())
        graph[i].append([a - 1, cost])

dp = [float('inf')] * (1 << n)


def solve(current):
    for i in range(n):
        if (1 << i & current):
            continue
        next_bit = current | (1 << i)
        total_price = dp[current] + price[i]
        if total_price < dp[next_bit]:
            dp[next_bit] = total_price
            diff = []
            for discount, discount_amount in graph[i]:
                next_price = max(price[discount] - discount_amount, 1)
                diff.append([discount, price[discount]])
                price[discount] = next_price
            solve(next_bit)
            for discount, discount_amount in diff:
                price[discount] = discount_amount


for i in range(n):
    dp[1 << i] = price[i]
    diff = []
    for discount, discount_amount in graph[i]:
        next_price = max(price[discount] - discount_amount, 1)
        diff.append([discount, price[discount]])
        price[discount] = next_price
    solve(1 << i)
    for discount, discount_amount in diff:
        price[discount] = discount_amount

print(dp[-1])
