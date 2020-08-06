# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        
        def makeTree(start,end,memo):
            
            lis = []
            if start>end:
                lis.append(None)
                return lis
            if start == end:
                lis.append(TreeNode(start))
                return lis
            if (start,end) in memo:
                return memo[(start,end)]
            
            for i in range(start,end+1):
                left = makeTree(start,i-1,memo)
                right = makeTree(i+1,end,memo)
                
                for lnode in left:
                    for rnode in right:
                        node = TreeNode(i)
                        node.left = lnode
                        node.right = rnode
                        lis.append(node)
                        
            memo[(start,end)] = lis
            return memo[(start,end)]
        
        if n==0:return []
        memo= {}    
        return makeTree(1,n,memo)