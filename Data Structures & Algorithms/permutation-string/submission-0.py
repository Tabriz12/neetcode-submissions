from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1c = Counter(s1)
        s2c = Counter(s2[:len(s1)])
        for i in range(len(s2)-len(s1)):

            if s1c==s2c:
                return True
            else:

                s2c[s2[i]]-=1
                s2c[s2[i+len(s1)]] = 1 + s2c.get(s2[i+len(s1)], 0)
        
        return s1c == s2c



        