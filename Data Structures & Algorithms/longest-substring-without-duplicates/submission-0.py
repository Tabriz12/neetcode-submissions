class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        seen = {}
        maxs = 0

        l = r = 0

        while r < len(s):

            if s[r] in seen and seen[s[r]] >= l:

                l = seen[s[r]] + 1
            
            maxs = max(r-l+1, maxs)
            
            seen[s[r]] = r

            r+=1
        
        return maxs
        

        # zxyzxyz



            

        