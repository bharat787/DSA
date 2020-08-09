# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, s: int) -> bool:
        
        if not root:
            return False
        
        ans = 0
        
        sub = s - root.val
        
        if(sub == 0 and root.left == None and root.right == None):
            return True
        
        if root.left is not None:
            ans = ans or self.hasPathSum(root.left, sub)
        if root.right is not None:
            ans = ans or self.hasPathSum(root.right, sub)
        
        return ans
        
        
        