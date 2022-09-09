t = int(input())
for i in range(t):
    n = int(input())
    a =  [0,1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

    for i in range(11,n+1):
        a.append(a[-1] +a[-5])

    print(a[n])