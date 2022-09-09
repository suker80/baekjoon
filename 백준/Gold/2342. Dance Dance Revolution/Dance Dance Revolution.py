command= list(map(int,input().split()))[:-1]
import sys
sys.setrecursionlimit(100000)
n = len(command)

dp = [[[0] * n for _ in range(5)] for _ in range(5)]

direction = {1:[2,4],2:[1,3],3:[2,4],4:[1,3]}

def solve(left,right,i):



    if i == n : return 0
    if dp[left][right][i] != 0 :return dp[left][right][i]
    c = command[i]
    dp[left][right][i] = min(solve(c,right,i+1) +calc(left,c), solve(left,c,i+1) + calc(right,c))

    return dp[left][right][i]



def calc(start,end):
    if start == end:return 1
    elif start == 0:
        return 2
    elif end in direction[start]: return 3
    else : return 4


solve(0,0,0)
print(dp[0][0][0])