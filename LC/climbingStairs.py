import collections
class Solution:
    def climbStairs(self, n: int) -> int:
        
        if(n == 1):
            return 1
        
        memo = collections.defaultdict(list)
        memo[1] = 1
        memo[2] = 2
        
        if n >= 3:
            for i in range(3, n+1):
                memo[i] = memo[i-1] + memo[i-2]
                
        return memo[n]
        