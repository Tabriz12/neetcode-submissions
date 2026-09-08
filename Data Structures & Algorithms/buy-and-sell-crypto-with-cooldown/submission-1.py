class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        '''
        [1,3,4,3,2,1]
        [1,3,4,0,4,1]
        [1,3,0,4,5]
        '''

        na = sell = 0

        buy = -prices[0] 

        for i in range(1, len(prices)):

            sell_prev = sell

            sell = prices[i] + buy

            buy = max(buy, na - prices[i])

            na = max(na, sell_prev)
        
        return max(na, sell)






























