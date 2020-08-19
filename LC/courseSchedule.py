class Solution:
    def canFinish(self, n: int, pre: List[List[int]]) -> bool:
        
        arrow = defaultdict(list)
        prereq = defaultdict(set)
        
        for x, y in pre:
            arrow [y].append(x) #courses must be taken y -> x
            prereq[x].add (y) #x, after y
            
        waiting = {e[0] for e in pre}
        
        front = {e[1] for e in pre} - waiting
        
        while front:
            new = []
            for y in front:
                for x in arrow[y]:
                    prereq[x].remove(y)
                    
                    if not prereq[x]:
                        new.append(x)
                        
                        waiting.remove(x)
            front = new
        if waiting:
            return False
        return True
        