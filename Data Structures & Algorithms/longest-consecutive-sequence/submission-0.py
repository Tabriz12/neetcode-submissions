class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        maxs = 0
        numset = set(nums)

        for n in numset:
            
            if not n-1 in numset:
                leng = 1
                while n + leng in numset:
                    leng+=1
                
                maxs = max(maxs, leng)
        
        return maxs
                





            



            



         