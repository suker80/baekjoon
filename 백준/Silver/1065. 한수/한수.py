N = int(input())

count = 0

if N < 100:
    print(N)
else :
    count = 99
    for i in range(100,N + 1):
        n = str(i)
        hun = int(n[0])
        ten = int(n[1])
        one = int(n[2])
        if hun - ten == ten -one:
            count +=1
    print(count)