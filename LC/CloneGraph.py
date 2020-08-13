"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        visited = {}
        
        def go(prev, cur):
            if cur not in visited:
                visited[cur] = Node(cur.val)
                for each in cur.neighbors:
                    go(cur, each)
            if prev:
                visited[prev].neighbors.append(visited[cur])
                
        go(None, node)
        return visited[node]  