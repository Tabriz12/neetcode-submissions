import math
class Solution:
    def numSquares(self, n: int) -> int:


        """

        15
        [1,4,9,]

        [0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0, 0]


        """


        res = int(math.sqrt(n))

        ch = [i**2 for i in range(1, res+1)]

        dp = [0] + [float('inf')]*n


        for i in range(1, len(dp)):

            for c in ch:


                if c > i:
                    break
                
                dp[i] = min(dp[i], dp[i-c] + 1)
        

        return dp[-1]




        