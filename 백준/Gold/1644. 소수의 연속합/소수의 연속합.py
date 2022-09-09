n = int(input())


def prime_list(N):
    prime = list()
    visited = [0]*(N+1)
    for i in range(2,N+1):
        if visited[i] == 0:
            prime.append(i)
            j = i
            while 1:
                if j > N:
                    break
                visited[j] = 1
                j += i
    return prime

sieve = prime_list(n)

s = 0
left, right = 0, 0
sums = 1
answer= 0
while right >=left  and right < len(sieve):

    if sieve[right] + s <=n:
        s += sieve[right]
        right += 1
    else :
        s -= sieve[left]
        left += 1
    if s== n:
        answer += 1
print(answer)