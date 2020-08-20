import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n==1:
            return True
        while(n):
            if n==2:
                return True
            n/=2
        return False