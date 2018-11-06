# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        queue = [root]
        result = []
        while queue:
            pNode = queue.pop(0)
            result.append(pNode.val)
            if pNode.left:
                queue.append(pNode.left)
            if pNode.right:
                queue.append(pNode.right)
        return result
            
