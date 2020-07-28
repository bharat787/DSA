# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        a = ListNode(-1, head)
        b = head
        c = head.next if head else None
        if not c:
            return head
        head = c
        while True:
            d = c.next # ⭐️ d is the beginning of the next pair to swap
            a.next = c
            b.next = c.next
            c.next = b
            if not d or not d.next: # ❌ nothing left to swap
                break
            a = b
            b = d
            c = d.next
        return head