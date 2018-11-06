
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def PrintTreeN(root):
    if not pRoot:
        print ("False")
    queue = [root]
    toBePrinted= 1
    nextLevel = 0
    while queue:
        pNode = queue[0]
        print(pNode.val,end='')
        if pNode.left:
            queue.append(pNode.left)
            nextLevel += 1
        if pNode.right:
            queue.append(pNode.right)
            nextLevel += 1
        queue.pop(0)
        toBePrinted -= 1
        if toBePrinted == 0:
            print('\n',end='') #print()
            toBePrinted = nextLevel
            nextLevel = 0
        else:
            print(" ",end='')
        
pRoot = TreeNode(8)
pRoot.left = TreeNode(6)
pRoot.right = TreeNode(10)
pRoot.left.left = TreeNode(5)
pRoot.left.right = TreeNode(7)
pRoot.right.left = TreeNode(9)
pRoot.right.right = TreeNode(11)

PrintTreeN(pRoot)
