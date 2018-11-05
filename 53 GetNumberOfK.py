# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        number = 0
        length = len(data)
        if data and length > 0:
            first = self.GetFirstK(data,length,k,0,length-1)
            last = self.GetLastK(data,length,k,0,length-1)
            if first > -1 and last > -1:
                number = last - first + 1
        return number
    
    def GetFirstK(self,data,length,k,start,end):
        if start > end:
            return -1
        
        middleIndex = int((start+end)/2)
        middleData = data[middleIndex]
        
        if middleData == k:
            if ((middleIndex > 0 and data[middleIndex-1] != k)\
                or middleIndex == 0):
                return middleIndex
            else:
                end = middleIndex - 1
        elif middleData > k:
            end = middleIndex - 1
        else:
            start = middleIndex + 1
        return self.GetFirstK(data,length,k,start,end)
    
    def GetLastK(self,data,length,k,start,end):
        if start > end:
            return -1
        middleIndex = int((start+end)/2)
        middleData = data[middleIndex]
        
        if middleData == k:
            if ((middleIndex < length-1 and data[middleIndex+1]!=k)\
                or middleIndex == length-1):
                return middleIndex
            else:
                start = middleIndex + 1
        elif middleData < k:
            start = middleIndex + 1
        else:
            end = middleIndex - 1
        return self.GetLastK(data,length,k,start,end)
    
            
        
        
