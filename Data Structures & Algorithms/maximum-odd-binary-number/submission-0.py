from collections import Counter
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:

        bis = Counter(s)

        res = ""
        while bis["1"] > 1:

            res+="1"

            bis["1"] -= 1
        


        res+= bis["0"] * "0" + "1"
        
        return res
        



        