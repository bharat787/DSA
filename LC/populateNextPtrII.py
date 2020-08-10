"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        stack = [root.left, root.right]
        
        while stack:
           # for i in stack:
            #    print(i.val)
            for i in range(len(stack)-1):
                if(stack[i] is not None and stack[i+1] is not None):
                    #print(stack[i].val, stack[i+1].val)
                    stack[i].next = stack[i+1]
                
            
            for i in range(len(stack)):
                l = stack.pop(0)
       
                if l is not None:
                    if l.left is not None:
                        stack.append(l.left)
                        print(l.left.val)
                    if l.right is not None:
                        stack.append(l.right)
                        print(l.right.val)
        
            
        return root