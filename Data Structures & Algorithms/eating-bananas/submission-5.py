import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1

        r = max(piles)+1

        k = float('inf')

        while l < r:


            mid = (l+r) // 2

            time = 0

            for p in piles:

                time += math.ceil(p/mid)
            
            if time <= h:

                k = min(k, mid)

                r = mid
            
            else:

                l = mid+1
        
        return k
            
            

