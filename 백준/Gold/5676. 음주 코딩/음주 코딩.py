def init(left, right, node):
    if left == right:
        if arr[left] == 0:
            tree[node] = 0
        elif arr[left] > 0:
            tree[node] = 1
        else:
            tree[node] = -1
        return tree[node]

    mid = (left + right) // 2

    m1 = init(left, mid, node * 2)
    m2 = init(mid + 1, right, node * 2 + 1)

    tree[node] = m1 * m2

    return tree[node]


def query(left, right, node, i, j):
    if i <= left and right <= j:
        return tree[node]
    if right < i or left > j:
        return 1
    mid = (left + right) // 2

    m1 = query(left, mid, node * 2, i, j)
    m2 = query(mid + 1, right, node * 2 + 1, i, j)

    return m1 * m2


def change(left, right, node, i, val):
    if not (left <= i and i <= right):
        return tree[node]

    if right == left and left == i:
        if val == 0:
            tree[node] = 0
        elif val > 0:
            tree[node] = 1
        else:
            tree[node] = -1
        return tree[node]

    mid = (left + right) // 2

    m1 = change(left, mid, node * 2, i, val)
    m2 = change(mid + 1, right, node * 2 + 1, i, val)

    tree[node] = m1 * m2

    return tree[node]


if __name__ == '__main__':

    import math

    import sys
    while True:
        try:
            n, k = map(int, input().split())
            input = sys.stdin.readline

            arr = [float('inf')] + list(map(int, input().split()))

            tree = [0] * (2 ** (math.ceil(math.log2(n)) + 1))


            init(1, n, 1)
            for i in range(k):
                op, a, b = input().rstrip().split()

                if op == 'P':
                    res = query(1, n, 1, int(a), int(b))

                    if res == 0:
                        print('0' , end='')
                    elif res > 0:
                        print('+', end='')
                    else:
                        print('-',end='')
                else:
                    change(1, n, 1, int(a), int(b))
            print('')
        except:
            break

