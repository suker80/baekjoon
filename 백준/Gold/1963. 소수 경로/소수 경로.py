import sys
from collections import deque


def prime_list(first, n):
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i + i, n, i):
                sieve[j] = False

    return sieve




def jump_1(start):
    e = int(str(start)[3])
    lst = []
    for i in range(-e, 10 - e):
        if i:
            temp = start + i
            if sieve[temp] == True:
                lst.append(temp)

    return lst


def jump_2(start):
    e = int(str(start)[2])
    lst = []
    for i in range(-e, 10 - e):
        if i:
            temp = start + i * 10
            if sieve[temp] == True:
                lst.append(temp)
    return lst


def jump_3(start):
    e = int(str(start)[1])
    lst = []
    for i in range(-e, 10 - e):
        if i:
            temp = start + i * 100
            if sieve[temp] == True:
                lst.append(temp)
    return lst


def jump_4(start):
    e = int(str(start)[0])
    lst = []
    for i in range(-e+1, 10 - e):
        if i:
            temp = start + i * 1000
            if sieve[temp] == True:
                lst.append(temp)
    return lst
t = int(input())

for _ in range(t):
    start, end = map(int, input().split())
    queue = deque([start])
    sieve = prime_list(1000, 10000)
    sieve[start] = 1
    flag = False
    while queue:
        current = queue.popleft()
        if current == end:
            print(sieve[current] - 1)
            flag = True
            break
            sys.exit()
        lst = jump_1(current)
        for s in lst:
            sieve[s] = sieve[current] + 1
            queue.append(s)
        lst = jump_2(current)
        for s in lst:
            sieve[s] = sieve[current] + 1
            queue.append(s)
        lst = jump_3(current)
        for s in lst:
            sieve[s] = sieve[current] + 1
            queue.append(s)
        lst = jump_4(current)
        for s in lst:
            sieve[s] = sieve[current] + 1
            queue.append(s)
    if not flag:
        print('impossible')

