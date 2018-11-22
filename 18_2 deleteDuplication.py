# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if pHead is None or pHead.next is None:
            return pHead
        pPreNode = pHead
        pNode = pHead
        pNewHead = pHead
        while pNode != None and pNode.next != None:
            if pNode.val != pNode.next.val:
                pPreNode = pNode
                pNode = pNode.next
            else:
                value = pNode.val
                while(pNode!=None and pNode.val == value):
                    if pNode == pNewHead:
                        pNewHead = pNewHead.next
                    pNode = pNode.next
                pPreNode.next = pNode
        return pNewHead
