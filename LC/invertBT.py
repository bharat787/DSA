# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        if not root:
            return
        
        stack = [root]
        
        while stack:
            l = stack.pop(0)
            
            temp = l.left
            l.left = l.right
            l.right = temp
            
            if l.left:
                stack.append(l.left)
            if l.right:
                stack.append(l.right)
                
        return root