class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        

        mas = cur = 0

        for i in nums:

            if i > 0:

                cur +=1

                mas = max(mas, cur)
            
            else:
                cur = 0

        return mas