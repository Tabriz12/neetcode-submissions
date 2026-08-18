from collections import Counter

from heapq import heapify, heappop_max, heappush_max
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:


        # [7, 3, 2, 3]

        cnts = Counter(tasks)

        max_freq = max(cnts.values())

        max_cnt = 0

        for _, v in cnts.items():
            if v == max_freq:
                max_cnt+=1
        


        return max(len(tasks), (max_freq-1) * (n+1) + max_cnt)
        

        



            



        

        





        