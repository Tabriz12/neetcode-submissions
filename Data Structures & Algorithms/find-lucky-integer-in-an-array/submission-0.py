from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:

        cnt = Counter(arr)

        mas = 0

        res = -1

        for k, v in cnt.items():


            if k == v and v > mas:

                mas = v

                res = k
        
        return res


        