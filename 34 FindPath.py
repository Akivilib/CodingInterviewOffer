
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # return 2-dim list
    def FindPath(self, root, expectNumber):
        # write code here
        if root is None:
            return []
        result = []
        path = []
        target = expectNumber
        result = self.FindOnePath(root,path,target,result)
        return result
    
    def FindOnePath(self,root,path,target,result):
        path.append(root.val)
        target -= root.val
        if target == 0 and root.left == None and root.right == None:
            onePath = []
            for items in path:
                onePath.append(items)
            result.append(onePath)
        if root.left:
            result = self.FindOnePath(root.left,path,target,result) 
        if root.right:
            result = self.FindOnePath(root.right,path,target,result)        
        if path:
            target += path[-1]
            path.pop()
        return result
