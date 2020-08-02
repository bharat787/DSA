# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        if not head or not head.next or k == 0:
            return head
        
        tail = head
        new_tail = head
        length = 1
        while tail.next:
            tail = tail.next
            length += 1
        tail.next = head
        new_k = length - (k % length)
        for _ in range(new_k-1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        return new_head