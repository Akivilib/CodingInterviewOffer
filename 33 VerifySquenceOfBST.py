# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if sequence is None or sequence == []:
            return False
        root = sequence[-1]
        length = len(sequence)
        for i in range(length):
            if sequence[i] > root:
                break
        for j in range(i,length):
            if sequence[j] < root:
                return False
        left = True
        right = True
        if i > 0:
            left = self.VerifySquenceOfBST(sequence[:i])
        if i < length - 1:
            right = self.VerifySquenceOfBST(sequence[i:length-1])
        return left and right
