def dfs(self, index, res, path, nums):
        res.append(list(path))        
        for i in range(index, len(nums)):
            path.append(nums[i])
            self.dfs(i+1, res, path, nums)
            path.pop()

def subsets(self, nums):
        res, path = [], []
        self.dfs(0, res, path, nums)
        return res