
from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:


        if k==0: return False

        i, j = 0, min(k, len(nums)-1)
        d = defaultdict(int)
        
        for n in nums[:j+1]:

            d[n]+=1
            if d[n]>1:
                return True
        
        while j+1 <= len(nums)-1:

            d[nums[i]]-= 1
            d[nums[j+1]] += 1

            if d[nums[j+1]] > 1:
                return True
            
            i+=1
            j+=1
        
        return False



        
        