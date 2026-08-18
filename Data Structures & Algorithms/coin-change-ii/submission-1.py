class Solution:
    def change(self, amount: int, coins: List[int]) -> int:


        dp = [1] + [0] * (amount)


        for coin in coins:

            for d in range(coin, amount+1):


                dp[d] += dp[d-coin]
        
        return dp[-1]
                




