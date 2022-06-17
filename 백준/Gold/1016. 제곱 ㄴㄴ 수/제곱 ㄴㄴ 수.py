n,m = map(int,input().split())
import math


lst = [i *i for i in range(2,int(m**0.5) + 1 )]

answer = [1] * (m-n+1)

for i in lst:
    idx =  0 if n % i == 0 else i-(n % i)

    while idx < m-n+1:
        answer[idx] = 0
        idx += i
print(sum(answer))
