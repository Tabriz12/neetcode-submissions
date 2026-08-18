from math import log
class Solution:

    def custom(self, n):

        res = 0
        while n > 0:

            pwr = int(log(n,2))

            n -= 2**pwr

            res+=1


        return res
    
    def BrianKernighan(self, n):


        res  = 0

        while n:

            n &= n-1
            res +=1
        
        return res

    def hammingWeight(self, n: int) -> int:

        

        
        return self.BrianKernighan(n)



        



        