# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
		def maxPathSum(self, root: TreeNode) -> int:
			self.maxvalue = float('-inf')
			def dfs(node):
				if node is None:
					return 0
				left = dfs(node.left)
				right = dfs(node.right)
				rootval = max(left,right)
				self.maxvalue = max(self.maxvalue, node.val+left+right)
				if rootval + node.val >= 0 :
					self.maxvalue = max(self.maxvalue, rootval + node.val)
					return rootval + node.val
				else:
					return 0
			dfs(root)
			return self.maxvalue