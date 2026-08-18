from heapq import heapify_max, heappush_max, heappop_max
from collections import Counter
class Solution:

    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        cnts = Counter(nums)
        return [elem for elem, _ in cnts.most_common(k)]


        








        