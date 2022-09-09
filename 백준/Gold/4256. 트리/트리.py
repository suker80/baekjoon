t = int(input())
from collections import deque
class Node:

    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val

def postorder(node):
    if node.left is not None:
        postorder(node.left)
    if node.right is not None:
        postorder(node.right)
    print(node.val,end = ' ')

def solve(root,start,end):

    if start-end == 0 :
        visit[pre_idx[root]] = True
        return Node(root)

    root_idx = idx[root]
    visit[pre_idx[root]] = True
    current = Node(root)

    left_root = preorder[pre_idx[root]+1]

    if root_idx != start:
        left = solve(left_root,start,root_idx-1)
        current.left =left

    right_root_idx = -1
    for i in range(n):
        if not visit[i]:
            right_root_idx = i
            break
    if right_root_idx == -1:
        return current
    right_root = preorder[right_root_idx]
    in_right_idx = idx[right_root]
    if end >= in_right_idx:
        right = solve(right_root,root_idx+1,end)
        current.right=right
    return current


for _ in range(t):
    n = int(input())
    preorder = list(map(int, input().split()))
    visit = [False] * n
    inorder = list(map(int, input().split()))
    idx = {}
    for i, item in enumerate(inorder):
        idx[item] = i
    pre_idx = {}
    for i , item in enumerate(preorder):
        pre_idx[item]=i
    root = preorder[0]
    head= solve(root,0,n-1)
    postorder(head)
    print('')











