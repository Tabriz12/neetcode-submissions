from heapq import heapify_max, heappush_max, heappop_max
from collections import Counter
class Solution:

    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        cnts = Counter(nums)
        h = []
        heapify_max(h)

        for ke, va in cnts.items():

            heappush_max(h, (va, ke))
        
        res = []
        for _ in range(k):
            
            res.append(heappop_max(h)[1])
        
        return res


        








        