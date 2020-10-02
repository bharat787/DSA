class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        u = [1]
        m = [0 for i in range(len(primes))]
        print(m)
        
        for i in range(n-1):
            
            u.append(min([u[m[i]]*primes[i] for i in range(len(primes))]))
            
            val = u[-1]
            
            for i in range(len(m)):
                if val == u[m[i]]*primes[i]:
                    m[i] += 1
        print(u)        
        return u[-1]