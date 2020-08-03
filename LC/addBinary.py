class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        car = 0
        
        a = list(a)
        b = list(b)
        
        if(len(a) < len(b)):
            while(len(a) != len(b)):
                a.insert(0,0)
        else:
            while(len(b) != len(a)):
                b.insert(0,0)
        for i in range(len(a)):
            a[i] = int(a[i])
            b[i] = int(b[i])
            
        for i in range(len(a) - 1, -1, -1):
            a[i] += car + b[i]
            if(a[i] == 2):
                a[i] = 0
                car = 1
            elif(a[i] == 3):
                a[i] = 1
                car = 1
            elif(car == 1 and a[i] == 1):
                car = 0
        if(car == 1):
            a.insert(0, 1)
                
        s = ''
        
        for i in range(len(a)):
            s += str(a[i])
            
        return s