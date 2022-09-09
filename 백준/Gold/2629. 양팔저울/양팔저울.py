n = int(input())
import sys
input = sys.stdin.readline

arr  = list(map(int,input().split()))

test_num = int(input())
case = list(map(int,input().split()))

max_weight = sum(arr)

dp = [[0] * (500 * n + 1) for _ in range(n + 1)]


def solve(cur_num,cur_weight):




    if dp[cur_num][cur_weight] != 0:
        return

    dp[cur_num][cur_weight] = 1
    if cur_num >= n:
        return
    solve(cur_num + 1 ,cur_weight + arr[cur_num])
    solve(cur_num + 1, cur_weight )
    solve(cur_num + 1, abs(cur_weight - arr[cur_num]))

for test in case:
    solve(0,0)
    if test > 500 * n : print('N')
    elif dp[n][test] == 1: print('Y')
    else: print('N')