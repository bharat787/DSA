class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
         
        res = [0 for _ in range(0, len(nums))]
        indexes = []
        
        for index, value in enumerate(nums):
            indexes += [(index, value)]
        
        def merge(left, right):
            final, right_added = [], 0
            i, j = 0, 0
            
            while i < len(left) and j < len(right):
                if left[i][1] > right[j][1]:
                    final += [right[j]]
                    right_added += 1
                    j += 1
                else:
                    final += [left[i]]
                    res[left[i][0]] += right_added
                    i += 1
                    
            while j != len(right):
                final += [right[j]]
                j += 1
            
            while i != len(left):
                final += [left[i]]
                res[left[i][0]] += right_added
                i += 1
            
            return final
            
                  
        def divide(tuples):
            if len(tuples) == 1:
                return tuples
            
            mid = len(tuples)//2
            left = divide(tuples[0:mid])
            right = divide(tuples[mid:len(tuples)])
            
            return merge(left, right)
        
        if not nums:
            return []
        divide(indexes)
        return res
