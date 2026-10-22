class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        rs = sum(nums)

        ls = 0

        for i in range(len(nums)):

            if rs - nums[i] == ls:
                return i
            
            ls+=nums[i]
            rs-=nums[i]
        
        return -1
        