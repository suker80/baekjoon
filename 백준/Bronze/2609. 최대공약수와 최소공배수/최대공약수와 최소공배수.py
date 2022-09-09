n, m = map(int,input().split())

if n > m:
    a,b= n,m
else:
    a,b = m,n
# 유클리드 호제법  a > b 일때 a = bq + r 로 나타낼수있다 . gcd(a,b)  = gcd(b,r) 나머지가 0이 될때까지

while b != 0:
    r= a % b
    a= b
    b= r

print(a)
print(int((m*n)/a))