from itertools import combinations 

n = int(input())

arr = [list(map(int,input().split())) for i in range(n)]

min_dif = float('inf')

for i in range(1,n+1):
    for com in combinations(arr,i):
        mul_result = 1
        add_result = 0
        for c in com:
            mul_result *= c[0]
            add_result += c[1]
        result = abs(mul_result - add_result)
        min_dif = min(min_dif,result)

print(min_dif)