# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        if s is None or s == "":
            return False
        i = 0
        j = 0
        for k in range(len(s)):
            if i==0 and s[k] == ".":
                i = k
            elif i!=0 and s[k] == ".":
                return False
            elif j==0 and (s[k] == "e" or s[k] == "E"):
                j = k
            elif j!=0 and (s[k] == "e" or s[k] == "E"):
                return False
            elif s[k] != "." and s[k] != "e" and s[k] != "E" and (s[k] < "0" or s[k] > "9") and s[k] != "+" and s[k] != "-":
                return False
            
        if i == 0 and j == 0: #int
            isNum = self.scanInteger(s)
        elif i != 0 and j == 0: #float
            isNum = self.scanInteger(s[:i]) or self.scanUsignedInteger(s[i+1:])
        elif i == 0 and j != 0: # int + exp
            isNum = self.scanInteger(s[:j]) and self.scanInteger(s[j+1:])
        elif i!=0 and j!=0 and i < j: #float + exp
            isNum = self.scanInteger(s[:i]) or self.scanUsignedInteger(s[i+1:j]) and self.scanInteger(s[j+1:])
        elif i!=0 and j!=0 and i > j: #wrong string
            return False
        return isNum
    
    def scanUsignedInteger(self, s):
        if s == "":
            return False
        for i in range(len(s)):
            if s[i] >= "0" and s[i] <= "9":
                continue
            else:
                return False
        return True
    
    def scanInteger(self, s):
        if s == "":
            return False
        if s[0] == "+" or s[0] == "-":
            return self.scanUsignedInteger(s[1:])
        else:
            return self.scanUsignedInteger(s)

if __name__ == '__main__':
    a = Solution()
    print(a.isNumeric("1+23"))
           
