class Solution:
    def findMin(self, nums: List[int]) -> int:


        """

        [4,2,3]
        [2,3,4,1]

        """
        

        l = 0

        r = len(nums)-1

        """
        1. l0, r2
        2. l1, r2
        3. l4, r4

        """
        while l < r:

            mid = (l+r) // 2

            if nums[mid] > nums[r]:

                l = mid+1
            
            elif nums[mid] < nums[l]:

                r = mid
            
            else:
                break
        
        return nums[l]
        

        