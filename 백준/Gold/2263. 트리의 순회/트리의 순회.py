n = int(input())
inorder = list(map(int,input().split()))
post = list(map(int,input().split()))

import sys
sys.setrecursionlimit(300000)
class Node:
    def __init__(self,value,l_child=None,r_child = None):
        self.value = value
        self.l_child = l_child
        self.r_child = r_child

child = {}

root = post.pop()
idx = {}
for i,item in enumerate(inorder):
    idx[item] = i
start,end = 0 , n-1
def post_order(root,temp_inorder):

    start = temp_inorder[0]
    end = temp_inorder[1]
    if start - end == 0 :
        return Node(root)


    root_idx = idx[root]
    current = Node(root)

    right_inorder = [root_idx+1, end]
    # if not right_inorder:
    #     return current


    if end-root_idx >  0:
        current.r_child= post_order(post.pop(),right_inorder)


    left_inorder = [start,root_idx-1]
    if root_idx - start>0:
        current.l_child= post_order(post.pop(),left_inorder)



    return current




tree = post_order(root,[start,end])
answer = []
def preorder(node):
    if not node:
        return
    print(node.value,end= ' ')
    preorder(node.l_child)
    preorder(node.r_child)

preorder(tree)