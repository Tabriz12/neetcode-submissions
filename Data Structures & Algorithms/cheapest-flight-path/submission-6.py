
from collections import defaultdict, deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        adj_list = defaultdict(list)

        INF = float('inf')

        minis = [INF for _ in range(n)]

        for s,d,p in flights:

            adj_list[s].append((d , p))
        

        q = deque([(0, src)])
        

        res = INF
        stops = -1

        while stops <= k:


            for _ in range(len(q)):

                price, st = q.popleft()
                if st == dst:

                    res = min(res, price)

                for nei, cost in adj_list[st]:

                    if price+cost < minis[nei]:
                        q.append((price+cost, nei))
                        minis[nei] = price+cost
                
            
            stops+=1 # 0 (200,1) # 1 (500,3) (300,2)
        
        return res if res != INF else -1
                

        





        
        