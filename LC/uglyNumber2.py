class Solution:
    def nthUglyNumber(self, n: int) -> int:
        arr = [1]
        x, y, z = 0,0 ,0
        
        for i in range(n+1):
            arr.append(min(arr[x]*2,arr[y]*3,arr[z]*5))
            
            m = arr[-1]
            
            if m == arr[x]*2:
                x += 1
                
            if m == arr[y]*3:
                y += 1
            
            if m == arr[z]*5:
                z += 1
            
        return arr[n-1]