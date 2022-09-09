import sys
sys.setrecursionlimit(10000)
tree = []
for i in sys.stdin:
    tree.append(int(i))

class Node:
    def __init__(self,value,left=None,right=None):
        self.value= value
        self.right=  right
        self.left = left
def insert(current,node):
    if current.value < node.value:
        if current.right is None:
            current.right = node
        else:
            insert(current.right,node)
    elif current.value > node.value:
        if current.left is None:
            current.left = node
        else:
            insert(current.left,node)

def build_tree(tree):
    root = Node(tree[0])
    for value in tree[1:]:
        node =Node(value)
        insert(root,node)
    return root

def postorder(node):
    if node:
        left= node.left
        right = node.right
        postorder(left)
        
        postorder(right)
        print(node.value)

binary_tree = build_tree(tree)
postorder(binary_tree)