class Solution:


    def findmax(self, nums, st, k):

        maxval = float('-inf')
        maxi = -1
        for i in range(st, st+k):

            if nums[i] >= maxval:
                maxval = nums[i]
                maxi = i

        
        return (maxval, maxi)

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:


        l = 0

        maxi = -1

        maxval = float('-inf')

        res = []

        while l + k <= len(nums):

            if l > maxi:

                maxval, maxi = self.findmax(nums, l, k)
                res.append(maxval)
                
            else:

                if nums[l+k-1]>=maxval:

                    maxi = l+k-1
                    maxval = nums[l+k-1]
                
                res.append(maxval)
            
            l+=1
        
        return res




        