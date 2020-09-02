import math
from itertools import permutations
def ArrangementSum(n):
    
    arr = [i for i in range(n)]
    
    # def permute(arr):
    #     if len(arr) == 0:
    #         return []
            
    #     if len(arr) == 1:
    #         return [lst]
            
    #     l = []
        
    #     for i in range(len(arr)):
    #         m = arr[i]
            
    #         remLst = arr[:i] + arr[i+1:]
            
    #         for p in permute(remLst):
    #             l.append([m] + p)
    #     return l
        
    #perms = permute(arr)
    perms = list(permutations(range(1, n+1)))
    print(perms)
        
    maxm = -1
    
    def absol(lst):
        s = 0
        for i in range(len(lst) -1 ):
            s += abs(lst[i] - lst[i+1])
        return s
        
    for i in perms:
        cur = absol(i)
        if cur > maxm:
            maxm = cur
            
    return maxm
