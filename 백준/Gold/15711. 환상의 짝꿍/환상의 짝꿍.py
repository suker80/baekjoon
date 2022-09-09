t = int(input())

max_thieve = 2_000_001
thieves = [False] * max_thieve

for i in range(2, max_thieve):
    if not thieves[i]:

        for j in range(i + i, max_thieve, i):
            thieves[j] = True
thieves[1] = True
primes = [i for i in range(2, max_thieve) if not thieves[i]]

for i in range(t):
    a, b = map(int, input().split())
    s = a + b
    if s % 2 == 0:
        if s > 2:
            print("YES")
        else:
            print("NO")
    else:
        s -= 2
        if s > max_thieve:
            for p in primes:
                if s % p == 0:
                    print("NO")
                    break
            else:
                print("YES")
        else:
            if thieves[s]:
                print("NO")
            else:
                print("YES")
