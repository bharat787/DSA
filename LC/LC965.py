# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        stack = [root]
        l = []
        while stack:
            s = stack.pop(0)
            l.append(s.val)
            
            if s.left:
                stack.append(s.left)
            if s.right:
                stack.append(s.right)
                
        sl = set(l)
        if len(sl) == 1:
            return True
        return False