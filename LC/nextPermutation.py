
def nextPermutation(nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        if(size<2):
            return
        end = size - 2
        while(end>=0):
            start = size - 1
            print(start, end)
            while(start>end):
                if(nums[start]>nums[end]):
                    nums[start], nums[end] = nums[end], nums[start]
                    print(nums)
                    nums[end+1:] = reversed(nums[end+1:])
                    print(nums)
                    return
                start-=1
            end-=1
        nums.sort()
nextPermutation([1, 3, 5, 4])