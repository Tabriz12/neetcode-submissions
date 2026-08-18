class Solution:


    def __init__(self):

        self.ans = 0

    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        """

        sum(p) - sum(n) = target

        sum(p) + sum(n) = tot

        2*p = target+tot

        p = target+tot / 2



        [2,3,5,7]

        """


        if (sum(nums)+target) % 2 == 1 or abs(target) > sum(nums):

            return 0
        
        s = (sum(nums)+target)// 2 
        
        dp = [1] + [0] * s

        for n in nums:

            for j in range(s, n-1, -1):

                dp[j] += dp[j-n]
        
        return dp[-1]



        