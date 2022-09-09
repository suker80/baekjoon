def init(left,right,node,func,tree):

    if left == right :
        tree[node] = arr[left]
        return tree[node]
    mid = (left + right) // 2
    tree[node] = func(init(left,mid,node*2,func,tree) , init(mid+1,right,node*2+1,func,tree))
    return  tree[node]

def query(i,j,left,right,node,func,tree):

    if right < i or left > j :
        return float('inf') if func == min else 0

    if j >= right and i <= left :
        return tree[node]
    mid = (left + right) // 2

    return func(query(i,j,left,mid,node*2,func,tree) , query(i,j,mid + 1 ,right,node*2 + 1 ,func,tree))


if __name__ == '__main__':
    import sys, math

    n, m = map(int, input().split())

    input = sys.stdin.readline

    arr = [0]

    for i in range(n):
        arr.append(int(input()))

    min_tree = [0] * pow(2, math.ceil(math.log(n, 2)) + 1)
    max_tree = [0] * pow(2, math.ceil(math.log(n, 2)) + 1)

    init(1, n, 1, min, min_tree)
    init(1, n, 1, max, max_tree)

    for i in range(m):
        a,b = map(int,input().split())
        m1 = query(a,b,1,n,1,min,min_tree)
        m2 = query(a,b,1,n,1,max,max_tree)
        print(m1,m2)

