from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        c = Counter(s+t)

        for k, v in c.items():

            if v % 2: return k
        
