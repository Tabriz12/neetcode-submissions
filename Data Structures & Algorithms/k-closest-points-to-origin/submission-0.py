from heapq import heapify, heappop, heappush
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:


        minis = []
        heapify(minis)


        for point in points:

            dist = math.sqrt(point[0]**2 + point[1]**2)

            heappush(minis, (dist, point))
        

        return [heappop(minis)[1] for _ in range(k)]
        