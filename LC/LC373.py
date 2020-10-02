import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        if not nums1 or not nums2 or not k: return []
        i = j = 0
        minHeap = []
        
        for _ in range(k):
            if i < len(nums1) and j < len(nums2):
                if nums1[i] <= nums2[j]:
                    for x in nums2[j:]: heapq.heappush(minHeap, (nums1[i], x))
                    i += 1
                else:
                    for x in nums1[i:]: heapq.heappush(minHeap, (x, nums2[j]))
                    j += 1
        print(minHeap)
        return heapq.nsmallest(k, minHeap, key = sum)