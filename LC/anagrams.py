class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ret = []
        
        if(len(strs) == 0):
                return 0
        if(len(strs) == 1):
            return [strs]
        l = []
        
        l.append(set(strs[0]))
        
        for i in strs:
            if set(i) not in l:
                l.append(set(i))
                
        for i in range(len(l)):
            ret.append([])
            
        for i in strs:
            ret[l.index(set(i))].append(i)
        
            
        return ret