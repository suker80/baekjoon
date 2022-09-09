n,m = map(int,input().split())
from collections import defaultdict
dic = defaultdict(int)
arr= list(map(int,input().split()))
def solve():
    left, right = 0, n*max(arr)
    if len(arr) == 1:
        print(1)
        return
    while right > left :
        mid = (left+right) // 2
        s= 0

        temp = []
        for num in arr:
            s += mid//num +1
        dic[mid] = s
        if s < n :
            left = mid + 1
            continue
        else :
            right = mid
    if n>s: mid += 1

    count = n - dic[mid-1]
    for i,a in enumerate(arr):
        if mid % a == 0:
            count -= 1
            if count == 0:
                print(i+1)
                return


solve()


