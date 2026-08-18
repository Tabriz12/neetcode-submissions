class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:




        for idx, i in enumerate(digits[-1::-1]):

            digits[len(digits)-idx-1] = (digits[len(digits)-idx-1] + 1) % 10

            if digits[len(digits)-idx-1] != 0:

                return digits
        
        return [1] + digits



        

        




        