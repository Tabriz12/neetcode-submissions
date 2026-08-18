import math
class Solution:
    def reverseBits(self, n: int) -> int:


        #pow = math.ceil(math.log(n, 2))

        c = 31

        res = 0

        while c >= 0:

            rem = n % 2

            res += rem * (2**c)

            n = n // 2

            c-=1
        
        return res
        