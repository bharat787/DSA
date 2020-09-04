class Solution:
    def countBits(self, num: int) -> List[int]:
        ret = []
        
        for i in range(num + 1):
            ret.append(str(bin(i)).count('1'))

        return ret
    
        