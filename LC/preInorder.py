# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        stack = [root]
        #pre_order
        i = 1
        #in_order
        j = 0
        while i < len(preorder):
            node = TreeNode(preorder[i])
            if stack[-1].val != inorder[j]:
                stack[-1].left = node
                
            else:
                while stack and stack[-1].val == inorder[j]:
                    last_node = stack.pop()
                    j += 1
                last_node.right = node
            stack.append(node)
            i += 1
        return root