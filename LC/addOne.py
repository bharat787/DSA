class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        if(digits[-1] < 9):
            digits[-1] += 1
            return digits
        
        car = 1
        digits[-1] = 0
        for i in range(len(digits) - 2, -1, -1):
            digits[i] += car 
            if (digits[i]>9):
                digits[i] = 0
                car = 1
            else:
                car = 0
        if(car == 1):
            digits.insert(0, 1)
                
        return digits
            
            
        