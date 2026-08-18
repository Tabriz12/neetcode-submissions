from heapq import heapify_max, heappop_max
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        tuples = [(heights[i], names[i]) for i in range(len(names))]

        heapify_max(tuples)

        return [heappop_max(tuples)[1] for _ in range(len(names))]


        