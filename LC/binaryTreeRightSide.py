# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        
        
        if not root:
            return []
        
        stack = [root]
        ret = []
        
        while stack:
            l = []
            
            for i in range(len(stack)):
                ele = stack.pop(0)
                l.append(ele.val)
                if ele.left:
                    stack.append(ele.left)
                if ele.right:
                    stack.append(ele.right)
            ret.append(l)
            
        out = []
        for i in ret:
            out.append(i[-1])
        return out