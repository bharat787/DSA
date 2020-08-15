# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        
        output = []
        stack =[root]
        
        if not root:
            return None
        
        while stack:
            
            temp=stack.pop()
            
            output.append(temp.val)
            
            if temp.left:
                stack.append(temp.left)
                
            if temp.right:
                stack.append(temp.right)
         
        return output[::-1]