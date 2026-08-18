class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:


        nums.sort()
        res = []

        for idx, n in enumerate(nums):

            

            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue
            l = idx+1
            r = len(nums)-1

            

            while l < r:

                tot = nums[l] + nums[r] + n

                if tot == 0:
                    res.append(
                        [n, nums[l], nums[r]]
                    )
                    while l < r and nums[l+1] == nums[l] :
                        l+=1
                    
                    while l < r and nums[r-1] == nums[r]:

                        r-=1

                    l+=1
                    r-=1
                
                elif tot > 0:

                    r-=1
                else:
                    l+=1
            
        return res



                


        