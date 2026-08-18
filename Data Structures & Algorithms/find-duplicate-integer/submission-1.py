class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # [1, 2, 4, 5, 2]


        for n in nums:

            idx = abs(n) - 1

            if nums[idx] < 0:
                return abs(n)
            
            else:
                nums[idx] *= -1
                

            
        
        