# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return None
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree
        left = self.Convert(pRootOfTree.left)
        node = left
        while node and node.right:
            node = node.right
  
        if left:
            node.right = pRootOfTree
            pRootOfTree.left = node
        right = self.Convert(pRootOfTree.right)
        if right:
            pRootOfTree.right = right
            right.left = pRootOfTree
        return left if left else pRootOfTree
