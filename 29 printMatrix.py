# -*- coding:utf-8 -*-
class Solution:
    # return 2-dim list
    def printMatrix(self, matrix):
        # write code here
        if not matrix:
            return []
        start = 0
        rows = len(matrix)
        columns = len(matrix[0])
        result = []
        while(rows>start*2 and columns>start*2):
            endX = rows - 1 - start
            endY = columns - 1 - start
            for i in range(start,endY+1):
                result.append(matrix[start][i])
            if start < endX:
                for i in range(start+1,endX+1):
                    result.append(matrix[i][endY])
            if start < endX and start < endY:
                for i in range(endY-1,start-1,-1):
                    result.append(matrix[endX][i])
            if start < endX - 1 and start < endY:
                for i in range(endX-1,start,-1):
                    result.append(matrix[i][start])
            start += 1
        return result
