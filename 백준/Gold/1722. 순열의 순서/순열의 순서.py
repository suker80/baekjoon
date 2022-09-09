n  =int(input())
q = list(map(int,input().split()))

fact = [1] * 21
fact[0] = 1
for i in range(2,n+1):
    fact[i] = fact[i-1] * i 
if q[0] == 1:
    
    q= q[1] - 1
    nums = list(range(1,n+1))
    result = []
    for i in range(n,0,-1):
        d = q//fact[i-1]
        q= q % fact[i-1]

        pop = nums.pop(d)
        result.append(pop)
    print(*result)

else:
    q = q[1:]
    nums = list(range(1,n+1))
    result = 1 

    for i,v in enumerate(q):

        idx = nums.index(v)
        nums.pop(idx)
        result += idx * fact[n-i-1]
    print(result)