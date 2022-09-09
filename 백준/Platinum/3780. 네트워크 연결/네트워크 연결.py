t = int(input())

import sys

input = sys.stdin.readline
def find(a):
    if parent[a] == a:
        return a, 0
    current = 0
    if dist[a] == 0:
        current += abs(a-parent[a]) % 1000
    p, parent_dist = find(parent[a])
    current += parent_dist
    dist[a] += current

    parent[a] = p
    return parent[a],dist[a]


for _ in range(t):
    n = int(input())

    parent = list(range(n + 1))
    dist = [0] * (n + 1)
    while True:
        lst = input().split()
        if lst[0] == 'O':
            break

        op = lst[0]

        if op == 'E':
            a= int(lst[1])
            if dist[a] == 0:
                find(a)
                print(dist[a])
            else:
                p,d = find(a)
                print(dist[a])

        else:
            a, b = int(lst[1]), int(lst[2])

            parent[a] = b
