
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.min_stack = []
        
    def push(self, node):
        self.stack.append(node)
        minNum = self.min()
        if not minNum or node < minNum:
            self.min_stack.append(node)
        else:
            self.min_stack.append(minNum)

    def pop(self):
        if self.stack:
            self.min_stack.pop()
            return self.stack.pop()
        
    def top(self):
        if self.stack:
            return self.stack[-1]
            
    def min(self):
        if self.stack and self.min_stack:
            return self.min_stack[-1]
