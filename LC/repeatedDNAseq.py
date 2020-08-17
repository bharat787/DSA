class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res,codeset = set(), set()
        for i in range(0,len(s)-9):
            if s[i:i+10] in codeset:
                res.add(s[i:i+10])
            else:
                codeset.add(s[i:i+10])
                
                
        print (list(res))
        return list(res)