# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if not pushV:
            return False
        stack = []
        j = 0
        for i in range(len(pushV)):
            stack.append(pushV[i])
            while j < len(popV) and stack and stack[-1] == popV[j]:
                stack.pop()
                j+=1
        return (not stack)
