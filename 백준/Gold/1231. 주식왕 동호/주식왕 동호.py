from collections import deque

c, d, m = map(int, input().split())
stock = [list(map(int, input().split())) for _ in range(c)]
money = [0] * 500001
money[m] = m
max_money = m
d -= 1
for i in range(d):
    max_money = max(money)
    money[max_money] = max_money
    index = [_ for _ in range(c) if stock[_][i + 1] > stock[_][i]]
    for m in range(max_money, -1, -1):
        if not money[m]:
            continue
        for j in index:
            diff = stock[j][i + 1] - stock[j][i]
            if diff > 0 and m - stock[j][i] >= 0:
                money[m - stock[j][i]] = max(money[m - stock[j][i]], money[m] + diff)

max_money = max(money)
print(max_money)