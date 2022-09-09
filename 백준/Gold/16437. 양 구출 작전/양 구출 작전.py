n = int(input())

input = __import__('sys').stdin.readline
import sys
sys.setrecursionlimit(10 ** 8)

graph =[[] for _ in range(n)]


island = [0]* n
for i in range(1,n):
    op,a,b, = input().split()

    if op == 'S':
        island[i]= int(a)
    else:
        island[i] = -int(a)

    graph[int(b)-1].append(i)


dp =[0] * n

def dfs(start):

    if not graph[start] :
        return max(island[start],0)

    s = 0
    for node in graph[start]:

        s += dfs(node)

    return max(s + island[start],0)

print(dfs(0))
