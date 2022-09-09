n= int(input())

import sys
input = sys.stdin.readline
from collections import defaultdict
rank = defaultdict(int)
rank_list = defaultdict(list)
node = defaultdict(lambda : None)

parent = defaultdict(int)



for i in range(n):
    p,l,r = map(int,input().split())
    node[p] = {'l':l,'r':r}

    parent[l] = p
    parent[r] = p



column  = [0]*(n+1)

idx = 1
max_rank = 0
def inorder(current,rank):
    global idx
    global max_rank

    max_rank = max(max_rank,rank)

    rank_list[rank].append(current)

    l,r = node[current]['l'] , node[current]['r']

    if l != -1:
        inorder(l,rank+1)

    column[current] = idx
    idx += 1
    if r != -1:
        inorder(r,rank+1)
for i in range(1,n+1):
    if parent[i] == 0:
        root = i
        break

inorder(root,0)
answer= 0
level = 0

for i in range(max_rank+1):
    lst = [column[j] for j in rank_list[i]]
    if max(lst) - min(lst) + 1 > answer:
        answer = max(lst) - min(lst) + 1
        level = i
print(level+1,answer)





