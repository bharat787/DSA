# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
        if not root:
            return []
        
        stack =  [root]
        ret = []
        
        while stack:
            l = stack.pop()
            
            if l:
                ret.append(l.val)
                stack.append(l.right)
                stack.append(l.left)
                
        return ret
    