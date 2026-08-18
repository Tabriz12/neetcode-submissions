class Solution:
    def canJump(self, nums: List[int]) -> bool:
        

        maxd = 0


        for i, n in enumerate(nums):

            if i > maxd:

                return False
            
            maxd = max(i+n, maxd)
    
        return True