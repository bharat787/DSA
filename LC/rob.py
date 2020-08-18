class Solution:
    def rob(self, nums: List[int]) -> int:
        
        s1 = s2 = 0
        
        if len(nums) > 0:
            s1 = nums[0]
        if len(nums) >= 2:
            s2 = max(s1, nums[1])
            
        for i in range(2, len(nums)):
            temp = s2
            s2 = max(s1 + nums[i], s2)
            s1 = temp
            
            
        return max(s1, s2)