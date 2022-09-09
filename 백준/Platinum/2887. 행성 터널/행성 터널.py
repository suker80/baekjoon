n = int(input())
import sys
input =sys.stdin.readline
cost  = []


def find(x):
    if x != parent[x]:
        return find(parent[x])
    return parent[x]

def union(a,b):

    parent_a = find(a)
    parent_b = find(b)

    if parent_b != parent_a:

        if parent_b > parent_a:
            parent[parent_a] = parent_b
        else:
            parent[parent_b] = parent_a

            

for i in range(n):
    x,y,z = map(int,input().split())
    cost.append([x,y,z,i])

min_cost = []
for i in range(3):
    cost.sort(key=lambda x:x[i])

    for j in range(n-1):
        min_cost.append([abs(cost[j][i] - cost[j+1][i]),cost[j][3],cost[j+1][3]])


min_cost.sort()

parent = list(range(n))

answer = 0

for i in range(len(min_cost)):
    c,a,b = min_cost[i]

    if find(a) != find(b):
        union(a,b)
        answer += c

print(answer)









