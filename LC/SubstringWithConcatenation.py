class Solution:
    

    def findSubstring(self, s: str, lst: List[str]) -> List[int]:
        def permutation(lst):
    
            if(len(lst) == 0):
                return []
            if(len(lst) == 1):
                return [lst]

            l = []

            for i in range(len(lst)):
                m = lst[i]
                remLst = lst[:i] + lst[i+1:]

                for p in permutation(remLst):
                    l.append([m] + p)

            return l
        
        possible = permutation(lst)
        ret = []
        for l in possible:
            test = ''
            for each in l:
                test += each
           # print(test)
            for i in range(0,len(s) - len(test)+1):
                #print(s, s[i:])
                try:
                    m = s[i:].index(test) + i
                    i+=len(test)
                    if m not in ret:
                        ret.append(m)
                except:
                    continue

        return ret
        
        