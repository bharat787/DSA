# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
              
        
        def merge2list(a, b):
            if a==None:
                print('first argument was none')
                return b
            if b==None:
                print('second argument was none')
                return a 
            if a.val<b.val:head,prev,a=a,a,a.next
            else:head,prev,b=b,b,b.next
            while a!=None and b!=None:
                if a.val<b.val:
                    prev.next=a
                    prev,a=a,a.next
                else:
                    prev.next=b
                    prev,b=b,b.next
            if a!=None:prev.next=a
            if b!=None:prev.next=b
            return head
        
        k = len(lists)
          
    
        if(k == 0):
            retll = ListNode("")
            retll.next = None
            return retll
        else:
            #ret = lists[0]
            #print(ret)
            interval = 1
            for i in range(0, k-interval, interval * 2):
                lists[i] = merge2list(lists[i], lists[i+1])
                interval *= 2

            return lists[0]