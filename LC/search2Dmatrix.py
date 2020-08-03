class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if(len(matrix) == 1):
            if(matrix[0] == []):
                return False
        
        for i in range(len(matrix)):
            if(target <= matrix[i][-1]):
                if(target in set(matrix[i])):
                    return True
                
        return False