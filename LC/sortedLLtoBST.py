class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        
        nums = []
        
        l = head
        while(l != None):
            nums.append(l.val)
            l = l.next
            
        def make(root):
            if not root:
                return None

            middle = int(len(root) / 2)

            tree = TreeNode(root[middle],make(root[0:middle]),make(root[middle + 1:]))
            return tree
        
        return make(nums)