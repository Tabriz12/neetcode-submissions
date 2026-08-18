class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        mult = 1
        zero = 1
        zero_ind = -1
        res = []

        for i, n in enumerate(nums):

            if n == 0:
            
                if mult == 0:

                    return [0] * len(nums)
                
                else:

                    res.extend([0]*i)
                    res.append(mult)
                    zero = mult
                    zero_ind = i
                    mult = 0
            
            else:
                if not mult:
                    res.append(0)
                    zero *=n
                else:
                    mult = n * mult
            
        if mult:
            return [mult//n for n in nums]


        
        else:
            res[zero_ind] = zero
            return res
        


        