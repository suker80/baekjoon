t= int(input())
import sys
input = sys.stdin.readline
from collections import deque
for _ in range(t):

    p = input()
    n= int(input())
    arr= input()[1:-2].split(',')
    arr =deque(arr)

    if not n:
        arr = deque([])
    flag= True
    r_count = 0
    for op in p:
        if op == 'R':
            r_count += 1

        elif op== 'D':

            if arr:
                if r_count % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()
            else:
                print('error')
                flag= False
                break
    else:
        if r_count %2 == 1:
            arr.reverse()
    if flag:
        answer = ','.join(arr)
        print('[' + answer + ']')

