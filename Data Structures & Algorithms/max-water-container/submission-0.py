class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0

        r = len(heights)-1

        a = 0

        while l < r:

            a = max(a, (r-l)*min(heights[l], heights[r]))

            if heights[r] > heights[l]:

                l+=1
            
            else:
                r-=1
        
        return a

            


        