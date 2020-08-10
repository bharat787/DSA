# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return root
        stack = [root]
        cur = None
        while stack:
            root = stack.pop()
            prev = cur
            cur = root
            if prev:
                prev.right, prev.left = cur, None
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)