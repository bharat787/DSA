class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        #we watch the data from bottom to top
        for i in range(len(triangle) -1, 0, -1):
		
			#find the smaller near num in the lower line and add it to the upper line
            for j in range(i):
                triangle[i-1][j] = triangle[i-1][j] + min(triangle[i][j], triangle[i][j+1])
		#the top point will be the shortest length.
        print(triangle)
        return triangle[0][0]
            