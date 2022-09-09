import sys
n, k  = map(int,input().split())
if n== 1 or k == 0 : 
    print(1)
    sys.exit()
arr = [[0]*(1012) for _ in range(1012)]
arr[1][1] = 1
arr[2][1:3] = [2,1]

for i in range(3,n+1):
    arr[i][1] = i
    for j in range(2,i+1):

        arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
print(arr[n][k] % 10007)