t = int(input())
n = 10000

sieve = [True] * n
m = int(n ** 0.5)
for i in range(2, m + 1):
    if sieve[i] == True:
        for j in range(i + i, n, i):
            sieve[j] = False

sieve = [i for i in range(2, n) if sieve[i] == True]

for _ in range(t):
    even_num = int(input())

    min_val = [10000, 0]
    for i in range(len(sieve)):
        if (even_num - sieve[i]) in sieve:
            if min_val[0] > abs(even_num - (sieve[i] * 2)):
                min_val[0] = abs(even_num - (sieve[i] * 2))
                min_val[1] = (sieve[i], even_num - sieve[i])
    print(*min_val[1])