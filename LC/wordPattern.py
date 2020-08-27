class Solution:
    def wordPattern(self, pattern: str, string: str) -> bool:
        
        if not string:
            return False
        
        l1 = list(pattern)
        l2 = list(string.split(' '))
        
        if len(l1) != len(l2):
            return False
        seen = []
        dictionary  = {}
        
        s1 = set(l1)
        s2 = set(l2)
        if len(s1) != len(s2):
            return False
        
        for i in range(len(l1)):
            if l1[i] not in seen:
                seen.append(l1[i])
                dictionary[l1[i]] = l2[i]
        
        for i in range(len(l1)):
            if(l2[i] != dictionary[l1[i]]):
                return False
            
        return True