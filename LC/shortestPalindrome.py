class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
      
        ptr1 = 0
        ptr2 = len(s) -1
        
        while(ptr2>ptr1):
            
            if s[ptr1:ptr2+1] == s[ptr1:ptr2+1][::-1]:
                break
            ptr2 -= 1
            
        return s[ptr2+1:][::-1] + s