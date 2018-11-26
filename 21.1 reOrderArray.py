# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        if array is None or len(array) == 0:
            return []
        pBegin = 0
        pEnd = len(array)-1
        while pBegin < pEnd:
            while pBegin < pEnd and array[pBegin] & 1 == 1:
                pBegin += 1
            while pBegin < pEnd and array[pEnd] & 1 == 0:
                pEnd -= 1
            if pBegin < pEnd:
                temp = array[pBegin]
                array[pBegin] = array[pEnd]
                array[pEnd] = temp
        return array
