class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        dp = []
        rows = len(matrix)
        cols = len(matrix[0])

        def replace(r, c):


                for i in range(cols):
                    matrix[r][i] = 0
                for i in range(rows):
                    matrix[i][c] = 0


        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if(matrix[row][col] == 0):
                    dp.append([row, col])

        for i in range(len(dp)):
            replace(dp[i][0], dp[i][1])

        print("matrix", matrix)