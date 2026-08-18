from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        res = []

        for strng in strs:
            found = False
            for grp in res:

                if Counter(grp[0]) == Counter(strng):

                    grp.append(strng)
                    found = True
                    break
            if not found:
                res.append([strng])
        
        return res