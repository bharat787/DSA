class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1:
            return [[1]]
        
        ret = [[0 for i in range(n)] for i in range(n)]
        
        top = left = 0
        bottom = right = n - 1
        k = 1
        while top <= bottom and left <= right:
            
            for i in range(left,right+1):
                ret[top][i] = k
                k += 1
                
            top += 1
            
            for i in range(top, bottom+1):
                ret[i][right] = k
                k+=1
                
            right -=1
            
            for i in range(right, left-1, -1):
                ret[bottom][i] = k
                k += 1
                
            bottom -= 1
            
            for i in range(bottom, top-1, -1):
                ret[i][left] = k
                k += 1
                
            left += 1
            
        return ret
                
            
        