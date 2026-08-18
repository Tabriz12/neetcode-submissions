class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:


        """

        [5,6,7,8,9, 1, 3, 4]


        [7, 8 , 1, 3, 9, 6]
        """

        dp = [1] * len(nums)
        ans = 1

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

            ans = max(ans, dp[i])

        return ans









        