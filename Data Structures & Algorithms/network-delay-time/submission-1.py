from heapq import heapify, heappop, heappush
class Solution:


    def dijkstra(self, times, n, k):

        dst = [float('inf')] * (n+1)

        dst[k] = 0

        routes = [[] for _ in range(n+1)]

        for s,d,t in times:

            routes[s].append([d,t])
        
        h = [[0, k]]

        heapify(h)


        while h:

            t, s = heappop(h)

            for dest, dly in routes[s]:

                if t+dly < dst[dest]:

                    dst[dest] = t + dly
                    heappush(h, [t+dly, dest])
        
        tot = max(dst[1:])

        return -1 if tot == float('inf') else tot


    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        return self.dijkstra(times, n, k)

        
            

        
        


        










        