import sys
import math

mod = 1000000007
def init(left, right, node):
    if left == right:
        tree_list[node] = arr[left]
        return tree_list[node]
    mid = (left + right) // 2
    m1 = init(left, mid, node * 2)
    m2 = init(mid + 1, right, node * 2 + 1)

    tree_list[node] = ((m1 % mod) * (m2 % mod)) % mod
    return tree_list[node]


def update(idx, value, left, right, node):
    if idx < left or idx > right:
        return tree_list[node]
    if left == right and left == idx:
        tree_list[node] = arr[idx] = value
        return tree_list[node]
    mid = (left + right) // 2
    m1 = update(idx, value, left, mid, node * 2)
    m2 = update(idx, value, mid + 1, right, node * 2 + 1)

    tree_list[node] = ((m1 % mod) * (m2 % mod ))% mod
    return tree_list[node]


def query(i, j, left, right, node):
    if right < i or left > j: return 1

    if j >= right and i <= left:
        return tree_list[node]
    mid = (left + right) // 2
    m1 = query(i, j, left, mid, node * 2)
    m2 = query(i, j, mid + 1, right, node * 2 + 1)

    return ((m1 % mod) * (m2 % mod ))% mod


if __name__ == '__main__':

    input = sys.stdin.readline
    n, m, k = map(int, input().split())

    arr = [1]

    for i in range(n):
        arr.append(int(input()))

    tree_list = [1] * (pow(2, math.ceil(math.log(len(arr), 2)) + 1) - 1)
    init(1, n, 1)

    for i in range(m + k):
        a, b, c = map(int, input().split())
        if a == 1:
            update(b, c, 1, n, 1)
        elif a == 2:
            print(query(b, c, 1, n, 1))
