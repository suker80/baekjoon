n = int(input())
table = [tuple(map(int,input().split())) for _ in range(n)]

result = 0

def dp(index,profit):
    global result
    if index > n:
        return
    elif index == n:
        result =  max(result,profit)
        return profit
    else:
        dp(index + 1 , profit)
        dp(index + table[index][0] ,profit + table[index][1] )
dp(0,0)
print(result)