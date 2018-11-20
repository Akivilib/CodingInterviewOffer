# -*- coding:utf-8 -*-
class Solution:
    # s, pattern is str
    def match(self, s, pattern):
        # write code here
        if s is None or pattern is None:
            return False
        elif s == "" and pattern == "":
            return True
        elif s != "" and pattern == "":
            return False
        elif s == "" and pattern != "":
            if len(pattern) >= 2 and pattern[1] == "*":
                return self.match(s,pattern[2:])  #"","a*a*"
            else:
                return False
        else:
            if len(pattern) >= 2 and pattern[1] == "*":
                if s[0] == pattern[0] or pattern[0] == ".":
                    return self.match(s,pattern[2:]) or self.match(s[1:],pattern)
                else:
                    return self.match(s,pattern[2:])
            else:
                if s[0] == pattern[0] or pattern[0] == ".":
                    return self.match(s[1:],pattern[1:])
                else:
                    return False
                
                
                
            
