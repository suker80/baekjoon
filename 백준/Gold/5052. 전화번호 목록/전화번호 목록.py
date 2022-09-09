t = int(input())
import sys

input = sys.stdin.readline
class node():
    def __init__(self,key,count=0):

        self.child={}

        self.key= key

for _ in range(t):
    n = int(input())
    head = node(None)
    answer = 'YES'
    nums = [list(map(str,input())) for _ in range(n)]
    nums.sort(key=len)
    for num in nums:
        cur = head
        for s in num:
            if '\n' in cur.child:
                answer= 'NO'
            if s not in cur.child:
                cur.child[s] = node(s)
            cur = cur.child[s]
    print(answer)
