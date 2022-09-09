n=int(input())
from collections import defaultdict

fibo_dict = defaultdict(lambda : -1)
fibo_dict[0] = 0
fibo_dict[1] = 1
fibo_dict[2] = 1

# f2n = (fn-1 + fn+1 )fn
# f2n-1 = (fn^2) + fn-1^2
def fibo(n):
    if fibo_dict[n] != -1:
        return fibo_dict[n]
    if n % 2 ==0:

        f = ((fibo(n//2-1)  % 1000000007) + (fibo(n//2+1) % 1000000007)) *(fibo(n//2) % 1000000007)
    else:

        f = (fibo((n+1)//2) %1000000007) **2 + (fibo((n+1)//2 -1 ) %1000000007)**2
    fibo_dict[n] = f
    return f% 1000000007

print(fibo(n))