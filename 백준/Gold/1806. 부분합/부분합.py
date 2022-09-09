N, S = map(int, input().split())
li = list(map(int, input().split()))

end = 0
summary = 0
shortest_len = float('inf')

for s in range(N):
    while summary < S and end < N:
        summary += li[end]
        end += 1
    if summary >= S:
        shortest_len = min(shortest_len, end - s)
    summary -= li[s]

if shortest_len == float('inf'):
    print(0)
else:
    print(shortest_len)