if len(nums) == 0:
            return 0
        elif len(nums) <= 3:
            return max(nums)
        else:
            def helper(nums):
                a = nums[0]
                b = max(nums[0],nums[1])
                for i in range(2,len(nums)):
                    res = max(b, a+nums[i])
                    a = b
                    b = res
                return res
            return max(helper(nums[:-1]), helper(nums[1:]))