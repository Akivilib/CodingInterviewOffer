# -*- coding: utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def PrintTreeZ(root):
    if not root:
        print ("False")
    stack = [[],[]]
    current = 0
    next = 1
    stack[current] = [root]
    while stack[0] or stack[1]:
        pNode = stack[current].pop()
        print(pNode.val,end='') 
        
        if current == 0:
            if pNode.left:
                stack[next].append(pNode.left)
            if pNode.right:
                stack[next].append(pNode.right)
        else:
            if pNode.right:
                stack[next].append(pNode.right)
            if pNode.left:
                stack[next].append(pNode.left)
                
        if not stack[current]:
            print()
            current = 1-current
            next = 1-next
        else:
            print(" ",end='')
        
pRoot = TreeNode(8)
pRoot.left = TreeNode(6)
pRoot.right = TreeNode(10)
pRoot.left.left = TreeNode(5)
pRoot.left.right = TreeNode(7)
pRoot.right.left = TreeNode(9)
pRoot.right.right = TreeNode(11)

PrintTreeZ(pRoot)
