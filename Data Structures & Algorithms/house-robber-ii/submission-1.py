class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) < 3:

            return max(nums)
        
         
        #nums = nums[:-1] if nums[0] > nums[-1] else nums[1:]

        res = nums[:2] + [0] * (len(nums)-3)

        # [10, 3, 8, 100, 90]
        for i in range(2, len(nums)-1):

            res[i] = nums[i] + max(res[i-2], res[max(0,i-3)])
        
        mas = max(res[-1], res[-2])


        nums = nums[::-1]

        res = nums[:2] + [0] * (len(nums)-3)

        for i in range(2, len(nums)-1):

            res[i] = nums[i] + max(res[i-2], res[max(0,i-3)])
        
        mas = max(res[-1], res[-2], mas)

        return mas
        

        #[3,2,1,6,4,2]
        