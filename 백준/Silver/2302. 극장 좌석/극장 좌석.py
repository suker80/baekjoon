n = int(input())
m = int(input())
vip=[0]
for i in range(m):
    vip.append(int(input()))
vip.append(n+1)

seat = list(range(1,n+1))

dp = [1,1,2,3]

for i in range(4,41):
    dp.append(dp[i-2] + dp[i-1])


if vip and m != n:
    result = 1 
    seat_term = []
    for i in range(m+1):
        seat_term.append(vip[i+1] - vip[i] -1)
    seat_term = [s for s in seat_term if s>0]
    
    for s in seat_term:
        result *= dp[s]
    print(result)
elif m==n:
    print(1)
else:
    print(dp[n])