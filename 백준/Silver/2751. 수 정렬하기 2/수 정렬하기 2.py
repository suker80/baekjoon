import sys
n = int(input())
input =sys.stdin.readline
arr = []
for i in range(n):
    arr.append(int(input()))
arr = sorted(arr)
print(*arr,sep="\n")