T = int(input())
A = []
N= 3 
for i in range(T):
    A.append([int(_) for _ in input().split(' ')])
    

def mergeSort(x):
    if len(x) > 1:
        mid = len(x)//2
        lx, rx = x[:mid], x[mid:]
        mergeSort(lx)
        mergeSort(rx)

        li, ri, i = 0, 0, 0
        while li < len(lx) and ri < len(rx):
            if lx[li] < rx[ri]:
                x[i] = lx[li]
                li += 1
            else:
                x[i] = rx[ri]
                ri += 1
            i += 1
        x[i:] = lx[li:] if li != len(lx) else rx[ri:]
        return x
for i in range(T):
    A[i] = mergeSort(A[i])
    print(A[i][-3])