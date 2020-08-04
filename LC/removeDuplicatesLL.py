# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        curr = head
        prev = None
        
        while(curr != None and curr.next != None):
            temp = curr.next
            
            if(curr.val == temp.val):
                while(temp != None and curr.val == temp.val):
                    temp = temp.next
                if(curr == head):
                    head = temp
                    curr = temp
                else:
                    curr = temp
                    prev.next = temp
            else:
                
                prev = curr
                curr = curr.next
                
                
        return head