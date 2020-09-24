class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) ==1:
            return True
#         else:
#             return False
        
        for i in range(1, len(nums)-1):
            if nums[i-1] == 0:
                nums[i] = 0
            else:
                nums[i] = max(nums[i-1]-1, nums[i])
            
        
        return nums[-2] >= 1