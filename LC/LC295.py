class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        self.leng = 0

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        self.nums = sorted(self.nums)
        self.leng += 1

    def findMedian(self) -> float:
        if self.leng %2 != 0:
            return(self.nums[int(self.leng/2)])
        else:
            ret = ((self.nums[int(self.leng/2)] + self.nums[int(self.leng/2) - 1])/2)
            return ret

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()