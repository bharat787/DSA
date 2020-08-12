# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        globalTotal = 0
        lis = []
        def helper(root, total, l):
            
            curtotal = total * 10 + root.val
            #print(curtotal)
            
            if root.left is None and root.right is None:
               # print('finally here', curtotal)
                l.append(curtotal)
                
            if root.left:
                helper(root.left, curtotal, l)
                
            if root.right:
                helper(root.right, curtotal, l)
                       
            
        helper(root, 0, lis)
       # print(lis)
        return sum(lis)