# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        
        self.root = root
        self.stack = [root]
        self.val = []
        if root:

            while self.stack:
                l = self.stack.pop()
                self.val.append(l.val)
                if l.right:
                    self.stack.append(l.right)
                if l.left:
                    self.stack.append(l.left)
        self.val = sorted(self.val)
       

    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.val.pop(0)

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.val:
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()