n = int(input())

train = [0]
for passenger in list(map(int,input().split())):

    if train:
        train.append(train[-1] + passenger)
    else:
        train.append(passenger)
k = int(input())

dp = [[0] * (n+1) for _ in range(4)]

for i in range(1,4):
    for j in range(1,n+1):
        dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - k] + train[j] - train[j - k])
print(dp[-1][-1])
