# -*- coding:utf-8 -*-
class Solution:
    # string
    def isNumeric(self, s):
        # write code here
        if len(s) <= 0:
            return False
        has_sign = False
        has_point = False
        has_e = False
        for i in range(len(s)):
            if s[i] == 'E' or s[i] == 'e':
                if has_e or i == len(s)-1:
                    return False
                else:
                    has_e = True
            elif s[i] == '+' or s[i] == '-':
                if i > 0 and s[i-1] != 'e' and s[i-1] != 'E':
                    return False
                else:
                    has_sign = True
            elif s[i] == '.':
                if has_point or has_e:
                    return False
                else:
                    has_point = True
            else:
                if s[i] < '0' or s[i] > '9':
                    return False
        return True
