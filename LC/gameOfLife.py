import copy
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        update = copy.deepcopy(board)
        
        def dfs(board, x, y):
            if(x<0 or x >= len(board) or y < 0 or y >= len(board[0])):
                return 0
            #print(x, y, board[x][y])
            
            return(board[x][y])
        
        def helper(board, x, y):
            
            s = dfs(board,x-1,y-1) + dfs(board,x-1,y) +dfs( board,x-1,y+1) + dfs(board,x,y+1) + dfs(board,x,y-1) + dfs(board,x+1,y+1) +dfs(board,x+1,y-1) + dfs(board,x+1,y)
            #print(x, y, s)
            if board[x][y] == 0:
                if s == 3:
                    update[x][y] = 1
            else:
                if s < 2:
                    update[x][y] = 0
                elif s > 3:
                    update[x][y] = 0
            #print('')
                    
        for i in range(len(board)):
            for j in range(len(board[0])):
                helper(board, i, j)
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = update[i][j]
            
        
            