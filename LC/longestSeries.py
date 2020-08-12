class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s = set(nums)
        maxlen = 1
        for n in nums:
            if n in s:
                mylen = 1
                up, down = n+1, n-1
                s.remove(n)
                while up in s:
                    mylen += 1
                    s.remove(up)
                    up += 1
                while down in s:
                    mylen += 1
                    s.remove(down)
                    down -= 1                    
                maxlen = max(maxlen, mylen)
        return maxlen