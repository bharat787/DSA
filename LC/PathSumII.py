# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        
        
        paths = []
        
        '''Recursive approach: DFS'''
        def dfs(root, sum, path):
            if root == None:
                return
            else:
                if root.val == sum and root.left == None and root.right == None:
                    paths.append(path + [root.val])
                    return paths
                else:
                    dfs(root.left, sum - root.val, path + [root.val])
                    dfs(root.right, sum - root.val, path + [root.val])
        dfs(root, sum, [])     
        return paths
		