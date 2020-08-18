class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        count = 0
        
        def search(grid,x,y):
            
            if (x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != "1"):
                return
            if grid[x][y] == "1":
                grid[x][y] = "0"
                search(grid, x+1, y)
                search(grid, x-1, y)
                search(grid, x, y+1)
                search(grid, x, y-1)
                
                
                
            
        for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if (grid[i][j] == "1"):
                        count += 1
                        search(grid, i, j)
        print(grid)
        return count
                