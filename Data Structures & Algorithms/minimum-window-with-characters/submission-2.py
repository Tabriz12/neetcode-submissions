from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        ct = Counter(t)
        cs = defaultdict(int)

        l = r = 0

        missing = len(ct)

        res = ""
        maxs = 1001

        for r in range(len(s)):
            c = s[r]

            cs[c]+=1

            if c in ct and cs[c] == ct[c]:

                missing -= 1
            

            while missing == 0:
                c = s[l]

                cs[c] -= 1

                if c in ct and cs[c] < ct[c]:

                    res = s[l:r+1] if maxs > (r-l+1) else res

                    maxs = len(res)

                    missing +=1
                
                l+=1
        
        return res
        

                


        
        


        