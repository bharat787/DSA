class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # if len(word) == 1:
        #     for i in board:
        #         if word in i:
        #             return True
        #         else:
        #             return False
                
        def dfs(x, y, index):
            if( x < 0 or x >= len(board) or y >= len(board[0]) or y < 0 or word[index] != board[x][y]):
                return False
            if index == len(word) -1:
                return True
            temp = board[x][y]
            board[x][y] = '0' 
            found = dfs(x+1, y, index+1) or dfs(x-1, y, index+1) or dfs(x, y+1, index+1) or dfs(x, y-1, index+1)
            board[x][y] = temp
            return found
        
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False
                
            