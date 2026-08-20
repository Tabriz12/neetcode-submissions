from collections import defaultdict as dd, deque
import bisect 

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        routes = dd(list)

        for s, d in tickets:

            routes[s].append(d)
        
        for s in routes:
            routes[s].sort(reverse=True)


        path = deque()


        def dfs(src):


            while routes[src]:

                dst = routes[src].pop()

                dfs(dst)
            

            path.appendleft(src)
        
        dfs("JFK")
        


        return list(path)





        


        