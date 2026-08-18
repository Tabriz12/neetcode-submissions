from heapq import *
class MedianFinder:

    def __init__(self):

        self.left = []
        self.right = []
        heapify_max(self.left)
        heapify(self.right)

    def addNum(self, num: int) -> None:
        
        if not self.right or num <= self.right[0]:

            heappush_max(self.left, num)

            if len(self.left) - len(self.right) > 1:

                heappush(self.right, heappop_max(self.left))
        
        else:
            heappush(self.right, num)

            if len(self.right) > len(self.left):
                heappush_max(self.left, heappop(self.right))



        
        

    def findMedian(self) -> float:

        if len(self.left) == len(self.right):

            return (self.left[0] + self.right[0]) / 2
        
        else:
            return self.left[0]
        
    

    """


    1,3,5
    """