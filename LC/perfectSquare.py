import math
class Solution:
    def numSquares(self, n: int) -> int:
        if math.sqrt(n) == int(math.sqrt(n)):
            return 1
        
        sqrs = [i**2 for i in range(1, int(math.sqrt(n))+1)][::-1]
        mins = float('inf')
        
        def helper(t, nums, idx):
            nonlocal mins
            l = len(nums)
			# If the current nums we're using >= the min that lead to the target return.
			# If t < 0 or > n return.
            if l >= mins or t < 0 or t > n:
                return
			# If by this stage our t == 0 we store the l, this only gets update if l < mins.
            if t == 0:
                mins = l
                return
            else:
			    # Recursively work through the sqrs.
                for i in range(idx, len(sqrs)):
                    helper(t-sqrs[i], nums + [sqrs[i]], i)
        
        helper(n, [], 0)
        return mins if mins != float('inf') else -1