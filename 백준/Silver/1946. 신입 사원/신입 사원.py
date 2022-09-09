t = int(input())
import sys

for _ in range(t):


    n = int(sys.stdin.readline())
    arr= [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
    arr.sort()

    m = arr[0][1]
    count = 1
    for i in range(n):
        if arr[i][1] < m:
            count += 1
        m = min(m,arr[i][1])
    print(count)
