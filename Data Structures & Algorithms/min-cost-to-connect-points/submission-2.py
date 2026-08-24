
from heapq import heappush, heappop
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:


        '''

        [0,0] [2, 2] [3,3]

        [2,2] [0,0] [5,5]

        '''

        adjm = [[] for _ in range(len(points))]

        for i in range(len(points)):

            a,b = points[i]

            for j in range(i+1, len(points)):

                c,d = points[j]

                dist = abs(a-c) + abs(b-d)

                adjm[i].append([j, dist])
                adjm[j].append([i, dist])

        

        tot = 0

        visited = set()

        h = [[0,0]]

        while len(visited) < len(points):


            dst, node = heappop(h)

            if node in visited:
                continue
            
            tot += dst

            visited.add(node)
            

            for nd, dt in adjm[node]:

                if nd not in visited:

                    heappush(h, [dt, nd])
                
        
        return tot
        