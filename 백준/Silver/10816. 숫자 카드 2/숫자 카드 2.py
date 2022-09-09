from collections import Counter

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
query = list(map(int, input().split()))
counter = Counter(arr)
print(' '.join(map(lambda x: str(counter[x]), query)))

