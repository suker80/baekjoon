a,b,c = map(int,input().split())

from collections import defaultdict

dic =defaultdict(lambda :-1)
dic[0] = 0
dic[1] = a %c
dic[2] = a**2%c

def power(n):
    if dic[n] != -1 :
        return dic[n]

    if n%2 == 0:
        p = (power(n//2)) * (power(n//2))
    else:
        p = (power((n-1)//2) %c ) *  (power((n-1)//2) %c) * dic[1] % c
    dic[n] = p
    return dic[n] % c

print(power(b))

