n = int(input())

arr = list(map(int, input().split()))
x = int(input())
tree = [[] for _ in range(n)]

for i, v in enumerate(arr):
    if v == -1 :
        root = i
        continue
    if i== x : continue
    tree[v].append(i)
answer = 0


def dfs(node):
    if node== x: return

    global answer
    if not tree[node]:
        answer += 1
    for next in tree[node]:
        dfs(next)
dfs(root)
print(answer)