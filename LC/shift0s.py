class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s = 0
        
        while nums.count(0) > 0:
            nums.remove(0)
            s += 1
            
        for i in range(s):
            nums.append(0)