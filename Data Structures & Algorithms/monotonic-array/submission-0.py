class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        diff = nums[-1] - nums[0]


        if diff > 0:

            for i in range(1, len(nums)):

                if nums[i] < nums[i-1]:
                    return False
            
        
        elif diff < 0:

            for i in range(1, len(nums)):

                if nums[i] > nums[i-1]:
                    return False
            

        else:

            for i in range(len(nums)):

                if nums[i] != nums[0]:
                    return False

        return True




        
        