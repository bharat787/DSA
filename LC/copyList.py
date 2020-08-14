"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
import copy
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        if not head: return head
        copy = Node(head.val)
        node_map, node_map[head], copy_head = {}, copy, copy, 
        while head:
            if head.next:
                if head.next in node_map: copy.next = node_map[head.next]
                else: node_map[head.next] = copy.next = Node(head.next.val)     
            if head.random:
                if head.random in node_map: copy.random = node_map[head.random]
                else: node_map[head.random] = copy.random = Node(head.random.val)
            node_map[head], head, copy = copy, head.next, copy.next

        return copy_head
