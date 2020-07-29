import copy
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        if(size<2):
            return
        end = size - 2
        while(end>=0):
            start = size - 1
            while(start>end):
                if(nums[start]>nums[end]):
                    nums[start], nums[end] = nums[end], nums[start]
                    nums[end+1:] = reversed(nums[end+1:])
                    return
                start-=1
            end-=1
        nums.sort()