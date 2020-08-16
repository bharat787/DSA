# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        if not headA or not headB:
            return None
        
        lena = 0
        lenb = 0
        
        la = lla = headA
        lb = llb = headB
        
        while la:
            la = la.next
            lena += 1
            
        while lb:
            lb = lb.next
            lenb += 1
            
        if lena < lenb:
            shift = lenb - lena
            
            for i in range(shift):
                llb = llb.next
        else:
            shift = lena - lenb
            
            for i in range(shift):
                lla = lla.next
                
        while(lla != llb):
            lla = lla.next
            llb = llb.next
            
        if lla != None:
            return lla
        
        return None
        
        