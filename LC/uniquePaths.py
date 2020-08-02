class Solution:
    
    
    def uniquePaths(self, m: int, n: int) -> int:
        
        mat = [[None for _ in range(n)] for _ in range(m)] 
        print(mat)
        
        # base case 
        mat[0] = [1 for _ in range(n)]
        for row in range(m): 
            mat[row][0] = 1 
        print(mat)
        # recursive 
        for row in range(1, m): 
            for col in range(1, n): 
                mat[row][col] = mat[row-1][col] + mat[row][col-1]
        print(mat)
        return mat[-1][-1]
    