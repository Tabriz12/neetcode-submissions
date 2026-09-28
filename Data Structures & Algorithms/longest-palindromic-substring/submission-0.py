class Solution:
    def longestPalindrome(self, s: str) -> str:


        ns = "_" + "_".join([c for c in s]) + "_"


        '''

        _a_b_a_b_d_

        '''

        mas = ns[:3]

        for i in range(2, len(ns)):

            l = r = i

            while l>0 and r<len(ns)-1 and ns[l-1] == ns[r+1]:

                l -= 1
                r += 1
            
            if r-l + 1 > len(mas):

                mas = ns[l:r+1]
        

        return "".join([c for c in mas if c!="_"])


                







        