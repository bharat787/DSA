import math
class Solution:
    def isHappy(self, n: int) -> bool:
        
        if n == 1:
            return True
        hashtable = []
        
        def squared(n):
            s = 0
            while n: 
                s += math.pow(n % 10, 2)
                n = int(n/10)
            print(s)
            return s
        
        while n != 1:
            
            if n not in hashtable:
                hashtable.append(n)
            else:
                break
            n = squared(n)
            
            
        if n != 1:
            return False
        
        return True