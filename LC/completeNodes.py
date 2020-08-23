# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        stack = [root]
        
        nodes = 0
        
        while stack:
            l = stack.pop(0)
            if l != None:
                nodes += 1
            
            if l.left:
                stack.append(l.left)
            if l.right:
                stack.append(l.right)
                
        return nodes
        
        