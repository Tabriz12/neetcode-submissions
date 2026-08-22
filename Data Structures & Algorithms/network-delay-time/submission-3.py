from heapq import heapify, heappop, heappush
class Solution:


    def BellmanFord(self, times, n, k):


        dst = [float('inf')] * (n+1)

        dst[k] = 0


        for _ in range(n-1):

            for s,d,t in times:

                if dst[s]+ t < dst[d]:

                    dst[d] = dst[s]+ t
        

        tot = max(dst[1:])

        return -1 if tot == float('inf') else tot





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
    

    def dfsing(self, times, n, k):

        dst = [float('inf')] * (n+1)

        dst[k] = 0

        routes = [[] for _ in range(n+1)]

        for s,d,t in times:

            routes[s].append([d,t])
        

        def dfs(src):

            for d,t in routes[src]:

                if dst[src] + t < dst[d]:

                    dst[d] = dst[src] + t

                    dfs(d)
        
        dfs(k)
        
        tot = max(dst[1:])

        return -1 if tot == float('inf') else tot






    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        return self.BellmanFord(times, n, k)

        
            

        
        


        










        