# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return None
        
        root = TreeNode(postorder[-1])
        stack = [root]
        inorder_index = len(inorder)-1
        postorder_index = inorder_index-1
        
        while postorder_index >= 0:
            v = postorder[postorder_index]
            node = TreeNode(v)
            parent = None
            postorder_index -= 1
            while stack and stack[-1].val == inorder[inorder_index]:
                inorder_index -= 1
                parent = stack.pop()
            
            if parent:
                parent.left = node
            else:
                stack[-1].right = node
                
            stack.append(node)
            
        return root