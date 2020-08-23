class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        s = set(nums)
        ret = []
        l = len(nums)
        for i in s:
            if nums.count(i) > l/3:
                ret.append(i)
                
                
        return ret