import collections
class Solution:
    def frequencySort(self, s: str) -> str:
        
        cnt = Counter(s)
        heap = [(-v, k) for k, v in cnt.items()]
        heapq.heapify(heap)
        print(heap)
        ans = []
        while(heap):
            root = heapq.heappop(heap)
            ans.append(root[1]*(-1*root[0]))
        return "".join(ans)