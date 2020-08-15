# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head: return None
        
        deq = collections.deque()
        node = head
        while node:
            deq.append(node)
            node = node.next
        
        front = True  # we start with the front
        last_node = None
        
        while deq:
            next_node = deq.popleft() if front else deq.pop()
            front = not front
            if last_node: last_node.next = next_node            
            last_node = next_node
        
        last_node.next = None        
        return head