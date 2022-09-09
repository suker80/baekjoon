n = int(input())

arr = list(map(int, input().split()))

graph = [[] for _ in range(n + 1)]

for idx, parent in enumerate(arr):
    if parent == -1:
        continue
    graph[parent].append(idx)

depth_graph = [[] for _ in range(n + 1)]


def dfs(node):
    # leaf node
    if not graph[node]:
        return 1

    current_child = []
    for next in graph[node]:
        child = dfs(next)
        current_child.append(child)

    current_child.sort(reverse=True)
    current_child = [child + idx for idx , child in enumerate(current_child)]
    return max(current_child)+ 1

print(dfs(0) -1 )

