class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        mas = float('-inf')

        roll = 0

        for n in nums:

            if n >= roll + n:

                roll = n
            
            else:

                roll += n
            

            mas = max(mas, roll)
        
        return mas


        