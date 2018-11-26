# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def EntryNodeOfLoop(self, pHead):
        meetingNode = self.MeetingNode(pHead)
        if meetingNode is None:
            return None
        
        nodeInLoop = 1
        pNode1 = meetingNode
        while pNode1.next != meetingNode:
            pNode1 = pNode1.next
            nodeInLoop += 1
        
        pNode1 = pHead
        pNode2 = pHead
        
        for i in range(nodeInLoop):
            pNode1 = pNode1.next
        while pNode1 != pNode2:
            pNode1 = pNode1.next
            pNode2 = pNode2.next
        return pNode1
        
    def MeetingNode(self, pHead):
        if pHead is None or pHead.next is None:
            return None
            
        pSlow = pHead.next
        pFast = pHead.next.next
        
        while pSlow != None and pFast != None:
            if pSlow == pFast:
                return pSlow
            pSlow = pSlow.next
            if pFast.next != None:
                pFast = pFast.next.next
        return None
        
