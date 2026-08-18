import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        prof = 0

        mini = sys.maxsize

        for n in prices:

            if n < mini:

                mini = n
            
            else:
                prof = max(prof, n-mini)
        
        return prof




        