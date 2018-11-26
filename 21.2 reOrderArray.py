# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        if array is None or array == []:
            return []
        for i in range(len(array)):
            if array[i] & 1 == 1:
                j = i - 1
                temp = array[i]
                while j >= 0 and array[j] & 1 == 0:
                    array[j+1] = array[j]
                    j -= 1
                array[j+1] = temp
        return array
