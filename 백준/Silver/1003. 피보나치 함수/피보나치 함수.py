n = int(input())
case = []
one = [0]*41
zero = [0] * 41

zero[0:3]= [1 ,0 ,1]
one[0:3] = [0,1,1]
for _ in range(n):
    case.append(int(input()))

def fibonacci(n):
    if n>=2:
        for i in range(3,n+1):
            zero[i]= zero[i-1] + zero[i-2]
            one[i] = one[i-1] + one[i-2]
for t in case :
    fibonacci(t)
    print(zero[t] , one[t])