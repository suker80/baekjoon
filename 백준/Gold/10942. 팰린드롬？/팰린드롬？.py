n = int(input())
import sys
input =  sys.stdin.readline
arr = list(map(int,input().split()))
m = int(input())
palindrome = [[0] * n for _ in range(n)]


for i in range(n):
    palindrome[i][i] = 1
for i in range(n-1):
    if arr[i] == arr[i+1]:
        palindrome[i][i+1] = 1

for j in range(2,n):
    for i in range(0,n-j):
        if arr[i] == arr[i+j] and palindrome[i+1][i+j-1] == 1:
            palindrome[i][i+j] = 1

for _ in range(m):
    a,b = map(int,input().split())


    print(palindrome[a-1][b-1])




