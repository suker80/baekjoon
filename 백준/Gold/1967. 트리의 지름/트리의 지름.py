n = int(input())
import sys
sys.setrecursionlimit(1000000)
input =sys.stdin.readline
tree = [ [] for _ in range(n+1)]
answer = 0
for _ in range(n-1):
    p,c,w= map(int,input().split())

    tree[p].append([c,w])

def dfs(node,weight):
    global answer
    max_weight = []
    if not tree[node]:
        return weight

    for n,w in tree[node]:
        max_weight.append(dfs(n,w))
        # print("node : {} weight {} max_weight {}".format(n,w,max(max_weight)))
    if len(max_weight) >= 2:
        max_weight.sort()
        answer = max(answer,max_weight[-2] + max_weight[-1])

    return max(max_weight) + weight

max_weight = dfs(1,0)
if len(tree[1]) == 1 :
    print(max(max_weight,answer))
else:
    print(answer)