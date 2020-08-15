class Solution:
    def reverseWords(self, s: str) -> str:
        
        if not s:
            return ""
        
        sentence = []
        l = ""
        for i in range(len(s)):
            
            if s[i] is not " ":
                l += s[i]
                print(l)
            else:
                sentence.append(l)
                
                l = ""
        sentence.append(l) 
        print(sentence)
        while sentence.count('') > 0:
            sentence.remove('')
        sentence = sentence[::-1]
        
        ret = ""
        
        for i in sentence:
            ret += i + " "
        
        return ret[:len(ret) -1]