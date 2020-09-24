class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
       
        nums = [i for i in range(1, 10)]
        res = []
        
        def backtrack(index, target, sub):
            if len(sub) == k:
                if target == 0:
                    res.append(sub)
            if index >= len(nums) or target < 0:
                return
            
            for i in range(index, len(nums)):
                if i  > index and nums[i] == nums[i-1]:
                    continue
                backtrack(i + 1, target - nums[i], sub+[nums[i]])
        
        backtrack(0, n, [])
        return res