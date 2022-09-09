n,target= map(int,input().split())

coins = [int(input())for _ in range(n)]

coins = sorted(coins,reverse=True)

count = 0
for i in range(len(coins)):
    
    if target // coins[i] > 0:
        count += target//coins[i]
        target = target % coins[i]
    if target == 0:
        print(count)
        break