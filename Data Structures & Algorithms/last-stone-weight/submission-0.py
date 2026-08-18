import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heapq.heapify_max(stones)

        while len(stones)>1:

            top1 = heapq.heappop_max(stones)
            top2 = heapq.heappop_max(stones)

            if top1-top2:
                heapq.heappush_max(stones, top1-top2)
        

        if stones: 
            return heapq.heappop(stones)
        
        else: return 0


        