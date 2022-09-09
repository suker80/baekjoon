t = int(input())

dp = [0] * 100
lst = [1, 10, 25]


def find(money, res):
    if money == 0:
        return res
    coin_res = float('inf')
    for coin in lst:
        if coin > money:
            break
        if money % coin == 0 :
            coin_res = min(coin_res, money // coin + res )
        else:
            coin_res = min(find(money - coin, 1 + res), coin_res)
    return coin_res


for i in range(1, 100):
    dp[i] = find(i, 0)

for _ in range(t):
    n = int(input())
    answer = 0
    while n:
        answer += dp[n % 100]
        n //= 100
    print(answer)
