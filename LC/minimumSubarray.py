class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        
        if not nums:
            return 0
        ans = 987654321
        left = 0
        sums = 0
        
        for i in range(len(nums)):
            sums += nums[i]
            while (sums >= s):
                ans = min(ans, i+1-left)
                sums -= nums[left]
                left += 1
                
        if ans != 987654321:
            return ans
        else:
            return 0