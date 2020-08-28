class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.mat = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        s = 0
        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                s += self.mat[i][j]
                
        return s


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)