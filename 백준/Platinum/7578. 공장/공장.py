n = int(input())
from collections import defaultdict

arr = [0] + list(map(int, input().split()))
dic = defaultdict(int)
b_arr = [0] + list(map(int, input().split()))
for idx in range(1, n + 1):
    val = b_arr[idx]
    dic[val] = idx

tree = [0] * (n + 1)


def query(x):
    ret = 0

    while x:
        ret += tree[x]
        x -= (x & -x)
    return ret


def update(x):
    while x <= n:
        tree[x] += 1
        x += (x & -x)


answer = 0
for i in range(1, n + 1):
    b_idx = dic[arr[i]]

    answer += query(n) - query(b_idx)
    update(b_idx)
print(answer)
