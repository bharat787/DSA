# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if not root:
            return []
        
        
        ret = []
        
        q = []
        
        q.append(root)
        zig = True
        
        while q:
            
            l = len(q)
            
            level = []
            
            for i in range(l):
                root = q.pop(0)
                level.append(root.val)
                if(root.left):
                    q.append(root.left)
                if(root.right):
                    q.append(root.right)
                        
            if(zig == False):
                level = level[::-1]
            zig = not zig
            ret.append(level)
            
                
        return ret