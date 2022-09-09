n,m,t = map(int,input().split())
from collections import deque
import sys
input = sys.stdin.readline
circles = [deque(map(int,input().split())) for _ in range(n)]


def calc():
    lst = []

    for i in range(n):
        for j in range(m):
            if circles[i][j] != 0:
                lst.append(circles[i][j])
    if not lst:
        return
    avg = sum(lst) / len(lst)
    for i in range(n):
        for j in range(m):
            if circles[i][j] != 0:
                if circles[i][j] > avg:
                    circles[i][j] -= 1
                elif circles[i][j] < avg:
                    circles[i][j] += 1

dir = [1,-1]
for _ in range(t):
    x_i,d_i,k_i = map(int,input().split())
    d_i = dir[d_i]
    flag = True
    temp = []
    for i in range(x_i - 1 ,n , x_i):
        circles[i].rotate(d_i *k_i)
    for k in range(n):
        for j in range(-1,m-1):
            if circles[k][j] == circles[k][j+1] and circles[k][j+1] != 0:
                flag = False
                temp.append([k,j+1])
                temp.append([k,j])

    for k in range(0,n-1):
        for j in range(m):
            if circles[k][j] == circles[k+1][j] and circles[k][j] != 0:
                flag = False
                temp.append([k+1, j ])
                temp.append([k, j])

    for y,x in temp:
        circles[y][x] = 0
    if flag == True:
        calc()



print(sum(sum(c) for c in circles))
