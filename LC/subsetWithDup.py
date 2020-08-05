class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        results = []
        
        def helper(i,path):
            if sorted(path) in results:
                pass
            else:
                results.append(sorted(path[:]))
            for x in range(i, len(nums)):
                path.append(nums[x])
                helper(x+1, path)
                path.pop()
        
        helper(0,[])
        return results