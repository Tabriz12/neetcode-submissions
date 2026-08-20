from collections import defaultdict as dd
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        routes = dd(list)

        for s, d in tickets:

            routes[s].append(d)
        
        for s in routes:
            routes[s].sort(reverse=True)


        path = []


        def dfs(src):


            while routes[src]:

                dst = routes[src].pop()

                dfs(dst)
            

            path.append(src)
        
        dfs("JFK")
        


        return path[::-1]





        


        