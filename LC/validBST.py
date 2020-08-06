# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack= []
        
        res = []
        
       
        while True:
            
            if root:
                stack.append(root)
                root = root.left
               # print(stack)
            
            elif stack:
                root = stack.pop()
                res.append(root.val)
               # print('res', res)
                root = root.right
                
            else:
                break
        flag = 0
        for i in range(len(res) -1 ):
            if(res[i+1] <= res[i]):
                flag = 1
                break
                
        if(flag == 1):
            return False
        else:
            return True
            