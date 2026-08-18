from math import log
class Solution:
    def hammingWeight(self, n: int) -> int:

        res = 0
        while n > 0:


            pwr = int(log(n,2))

            n -= 2**pwr

            res+=1


        return res


        



        