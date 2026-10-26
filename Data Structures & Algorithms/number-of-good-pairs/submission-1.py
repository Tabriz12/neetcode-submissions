from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        tots = Counter(nums)
        res = 0
        for _, v in tots.items():

            res += (v-1)*v // 2
        
        return res






        