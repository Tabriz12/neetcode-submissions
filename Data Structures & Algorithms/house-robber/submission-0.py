class Solution:
    def rob(self, nums: List[int]) -> int:

        """

        [2,5,1,0,7, 1]

        """

        if len(nums) < 3:
            return max(nums)

        res = nums[:2] + [0] * (len(nums)-2)

        for i in range(len(nums)):

            if i+2 < len(nums):

                res[i+2] = max(res[i+2], res[i]+nums[i+2])
            
            if i+3 < len(nums):
                res[i+3] = max(res[i+3], res[i]+nums[i+3])
        

        return max(res[-1], res[-2])
        

        

                



        
        

        


        
        