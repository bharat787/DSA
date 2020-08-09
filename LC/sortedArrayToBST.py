# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
       
        def make(root):
            if not root:
                return None

            middle = int(len(root) / 2)

            tree = TreeNode(root[middle],make(root[0:middle]),make(root[middle + 1:]))
            return tree
        
        return make(nums)
        