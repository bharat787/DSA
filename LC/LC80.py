class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i=0
        while i+2<len(nums):
            if nums[i]==nums[i+2]:
                nums.pop(i+2)
            else:
                i=i+1
        return len(nums)

#         s = set(nums)
#         ret = 0
#         for i in s:
#             ret += min(2, nums.count(i))
            
#         return ret