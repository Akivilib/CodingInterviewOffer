

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head is None or k <= 0:
            return None
        
        pBefore = head
        for i in range(k-1):
            if pBefore.next != None:
                pBefore = pBefore.next
            else:
                return None
        
        pBehind = head
        while pBefore.next != None:
            pBefore = pBefore.next
            pBehind = pBehind.next
        return pBehind
