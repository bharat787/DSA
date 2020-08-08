# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if not root:
            return []

        q = []
        ret = []
     
        q.append(root)
        
        while(q):
            l = len(q)
            
            level = []
            
            for i in range(l):
                root = q.pop(0)
                level.append(root.val)
                if(root.left):
                    q.append(root.left)
                if(root.right):
                    q.append(root.right)
                
                
            ret.append(level)
                
        return ret