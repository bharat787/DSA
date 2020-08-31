class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        s = set(i for i in range(n))
        
        for e in edges:
            if e[1] in s:
                s.remove(e[1])
        return list(s)