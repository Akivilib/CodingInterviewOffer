# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # return RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return None
        pNode = pHead
        # clone node
        while pNode:
            pCloned = RandomListNode(pNode.label)
            pCloned.next = pNode.next   #None
            pNode.next = pCloned
            pNode = pCloned.next
        # clone random
        pNode = pHead
        while pNode:
            pCloned = pNode.next
            if pNode.random:
                pCloned.random = pNode.random.next
            pNode = pCloned.next  #None
        # separate list
        pNode = pHead
        if pNode:
            pClonedNode = pNode.next
            pClonedHead = pHead.next
            pNode.next = pClonedHead.next
            pNode = pNode.next
        while pNode:
            pClonedNode.next = pNode.next
            pClonedNode = pClonedNode.next
            pNode.next = pClonedNode.next
            pNode = pNode.next
        return pClonedHead
