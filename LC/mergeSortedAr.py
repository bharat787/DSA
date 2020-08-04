class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while(len(nums1) != m):
            nums1.pop()
            
        nums1 += nums2
        nums3 = sorted(nums1)
        while(len(nums1) != 0):
            nums1.pop()
            
        for i in range(len(nums3)):
            nums1.append(nums3[i])
        print(nums1)
        