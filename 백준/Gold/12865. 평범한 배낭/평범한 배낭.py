n,k = map(int,input().split())

arr = [list(map(int ,input().split())) for i in range(n)]

bag = [[0] * (k+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,k+1):
        if arr[i-1][0] <= j:
            bag[i][j] = max(arr[i-1][1] + bag[i-1][j-arr[i-1][0]],bag[i-1][j])
        else:
            bag[i][j] = bag[i-1][j]

print(bag[n][k])