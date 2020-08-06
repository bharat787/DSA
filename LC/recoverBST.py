# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        misplaced = []
        stack = []
        cur = root
        pre = None
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            
            if pre:
                if pre.val > cur.val:
                    misplaced.append(pre)
                    misplaced.append(cur)
            pre = cur

            cur = cur.right

        x, y = misplaced[0], misplaced[-1]
        x.val, y.val = y.val, x.val