from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        tots = Counter(nums)
        res = 0
        for _, v in tots.items():

            for i in range(v):
                res+=i
        
        return res






        