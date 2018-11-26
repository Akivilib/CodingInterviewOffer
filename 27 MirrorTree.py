
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def Mirror(self, root):
        if not root:
            return
        if not root.left and not root.right:
            return
        
        temp = root.left
        root.left = root.right
        root.right = temp
        
        if root.left:
            self.Mirror(root.left)
        if root.right:
            self.Mirror(root.right)
 
