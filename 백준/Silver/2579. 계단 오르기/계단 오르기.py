n = int(input())
step = [int(input()) for i in range(n)]

if len(step) <3:
    print(sum(step))
else:
    dp=[step[0]]
    dp.append(step[0]+step[1])
    dp.append(max(step[1]+step[2],step[0]+step[2]))

    for i in range(3,n):
        dp.append(max(dp[i-2] + step[i], dp[i-3]+step[i-1] + step[i]))


    print(dp[-1])