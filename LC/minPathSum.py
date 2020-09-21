class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0
        if len(grid) == 1:
            return sum(grid[0])
        
        for i in range(len(grid)):
             for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    continue
                t1 = grid[i-1][j] if i > 0 else float('inf')
                t2 = grid[i][j-1] if j > 0 else float('inf')
                grid[i][j] += min(t1, t2)
                
        return grid[-1][-1]
        
        
            