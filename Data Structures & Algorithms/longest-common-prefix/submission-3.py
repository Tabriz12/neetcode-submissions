class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:


        res = strs[0]

        for s in strs[1:]:

            fin = min(len(s), len(res))
            if not fin:
                return ""

            for i in range(fin):

                if s[i] != res[i]:

                    if i == 0:
                        return ""
                    
                    else:

                        res = res[:i]
                        break
            else:
                res = res[:fin]
        
        return res
        