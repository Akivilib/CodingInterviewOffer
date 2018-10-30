# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def ReverseList(self, pHead):
        # define new prev,p,next,head
        pReversedHead = None
        pNode = pHead
        pPrev = None
        
        while (pNode != None):
            # save next
            pNext = pHead.next
            
            # find head
            if pNext == None:
                pReversedHead = pNode
            
            # reverse pointer
            pNode.next = pPrev
            
            # next 
            pPrev = pNode
            pNode = pNext
            
        return pReversedHead
