class Solution:
    def trap(self, height: List[int]) -> int:

        if len(height) < 3:

            return 0

        hl = height[0]
        hr = height[-1]
        l = 0
        r = len(height)-1

        tot = 0
        # l = 1 if hl < hr else 0
        # r = len(heights)-1 if l else len(heights)-2

        while l < r:


            if height[l] < height[r]:

                l+=1

                if height[l] >= hl:
                    hl = height[l]
                
                else:

                    tot += max(0, min(hl, hr) - height[l])
            else:
                r-=1

                if height[r] >= hr:
                    hr = height[r]
                
                else:

                    tot += max(0, min(hl, hr) - height[r])

        return tot



                







        