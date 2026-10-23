from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        res = ord(t[0])
        tot  = t[1:] + s
        for c in (tot):

            res^=ord(c)
        
        return chr(res)
        
