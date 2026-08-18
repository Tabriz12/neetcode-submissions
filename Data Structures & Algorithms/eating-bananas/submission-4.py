import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)

        while l < r:

            speed = (r+l) // 2
            tot = 0
            for p in piles:
                
                tot += math.ceil(p / speed)
            
            if tot <= h:
                r = speed
            
            else:
                l = speed + 1

        return r



        