n = int(input())
fib = [0] * 100
fib[0:3] =  [0, 1 , 1]
for i in range(3,n+1):
    fib[i] = fib[i-2] + fib[i-1]
print(fib[n])