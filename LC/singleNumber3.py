class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        if len(nums) == 1:
            return [nums[0]]
        xor = lambda x, y : x^y
        
        xor_result = reduce(xor, nums)
        print(xor_result)
        
        mask = xor_result & -xor_result
        print(mask)
        
        single_num_a, single_num_b = 0,0
        
        for number in nums:
            
            if mask&number:
                single_num_a ^= number
            else:
                single_num_b ^= number
                
        return [single_num_a, single_num_b]