# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack= []
        
        res = []
        
       
        while True:
            
            if root:
                stack.append(root)
                root = root.left
                print(stack)
            
            elif stack:
                root = stack.pop()
                res.append(root.val)
                print('res', res)
                root = root.right
                
            else:
                break
        
        return res