n = int(input())
import sys
input = sys.stdin.readline

class Node():
    def __init__(self,degree):
        self.child = {}
        self.degree = degree

head = Node(0)

def preorder(node):

    if node.child:
        for c in sorted(node.child):
            print('--' * node.child[c].degree + c)
            preorder(node.child[c])

for i in range(n):
    lst = list(map(str,input().rstrip().split()))
    l = lst[0]
    lst = lst[1:]
    cur = head
    for i,s in enumerate(lst):
        if not cur.child.get(s):
            cur.child[s] = Node(i)
        cur = cur.child[s]


preorder(head)

