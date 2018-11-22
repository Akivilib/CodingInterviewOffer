# -*- coding:utf-8 -*-
class Solution:
    # solution 1 
    def Power_1(self, base, exponent):
        # write code here
        if base == 0:
            return 0
        if exponent == 0:
            return 1
        elif exponent == 1:
            return base
        result = 1
        for i in range(abs(exponent)):
            result *= base
         return result if exponent > 0 else 1/result
    
    # solution 2 recursive method
    def Power_2(self, base, exponent):
        # write code here
        if base == 0:
            return 0
        if exponent == 0:
            return 1
        elif exponent == 1:
            return base
        n = abs(exponent)
        result = self.Power_2(base,n >> 1)
        result *= result
        if n & 0x1 == 1:
            result *= base
        return result if exponent > 0 else 1/result
    
    # solution 3 fast power
    def Power_3(self, base, exponent):
        # write code here
        if base == 0:
            return 0
        if exponent == 0:
            return 1
        elif exponent == 1:
            return base
        n = abs(exponent)
        result = 1
        b = base
        while n > 0:
            if n & 1 == 1:
                result *= b
            b *= b
            n = n >> 1 
        return result if exponent > 0 else 1/result
