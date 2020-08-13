class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or len(board) == 0:
            return
        
        rows = len(board)
        cols = len(board[0])
        
        
        def dfs(board, i, j):
            if(i < 0 or i>= rows or j < 0 or j >= cols or board[i][j] != 'O'):
                return
            if(board[i][j] == 'O'):
                board[i][j] = 'E'
            dfs(board, i+1, j)
            dfs(board, i-1, j)
            dfs(board, i, j+1)
            dfs(board, i, j-1)
            
            
        for i in range(rows):
            if board[i][0] == 'O':
                dfs(board, i, 0)
            if board[i][cols - 1 ] == 'O':
                dfs(board, i, cols - 1 ) 
                
        for i in range(cols):
            if board[0][i] == 'O':
                dfs(board, 0, i)
            if board[rows - 1][i] == 'O':
                dfs(board, rows - 1, i)
               # print(rows - 1, i)
                
        for i in range(rows):
            for j in range(cols):
                if(board[i][j] == 'O'):
                    board[i][j] = 'X'
                if(board[i][j] == 'E'):
                    board[i][j] = 'O'