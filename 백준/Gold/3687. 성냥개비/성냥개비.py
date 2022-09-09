t = int(input())
dic = {1: 2, 2: 5, 3: 5, 4: 4,
       5: 5, 6: 6, 7: 3, 8: 7,
       9: 6, 0: 6}
inf = 10 ** 102

min_dp = [inf] * 101
min_dp[2] = 1
min_dp[3] = 7
min_dp[4] = 4
min_dp[5] = 2
min_dp[6] = 6
min_dp[7] = 8
min_dp[8] = 10
min_dp[9] = 18
for i in range(10, 101):
    for key, val in dic.items():
        if key:
            min_dp[i] = min(min_dp[i], int(str(key) + str(min_dp[i - val])))
        min_dp[i] = min(min_dp[i], int(str(min_dp[i - val]) + str(key)))

for _ in range(t):
    n = int(input())
    max_answer = ''
    min_answer = ''

    max_dp = [0] * (n + 1)

    max_temp = n
    if n % 2 == 0:
        max_answer = '1' * (n // 2)
    else:
        max_answer = '7' + '1' * ((n // 2) - 1)
    print(min_dp[n], max_answer)
