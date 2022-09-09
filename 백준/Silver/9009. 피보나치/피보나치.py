fib =[0,1,1,2]

for i in range(3,100):
    fib.append(fib[i] + fib[i-1])

fib = [f for f in fib if f < 1000000000]

t = int(input())
for _ in range(t):
    n= int(input())
    arr = []
    while n>0:
        temp_fib = [f for f in fib if f<=n]
        arr.append(temp_fib[-1])
        n -= temp_fib[-1]
    arr.reverse()
    print(*arr)