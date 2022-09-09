n= int(input())
arr = list(map(int,input().split()))
import bisect
answer = 0

def mergeSort(x):
    global answer
    if len(x) > 1:
        mid = len(x)//2
        lx, rx = x[:mid], x[mid:]
        mergeSort(lx)
        mergeSort(rx)

        li, ri, i = 0, 0, 0
        while li < len(lx) and ri < len(rx):
            if lx[li] <= rx[ri]:
                x[i] = lx[li]
                li += 1
            else:
                x[i] = rx[ri]
                answer += (len(lx) - li)
                ri += 1
            i += 1
        x[i:] = lx[li:] if li != len(lx) else rx[ri:]
mergeSort(arr)
print(answer)