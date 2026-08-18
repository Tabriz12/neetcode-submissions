class Solution:
    def countBits(self, n: int) -> List[int]:

        """
        01
        1(0/1)
        11()

        0,1,1,2,1,2,2,3

        """

        dp = [0] * (n + 1)
        for i in range(n + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp


        