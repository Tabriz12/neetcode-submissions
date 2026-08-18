class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        res = (len(s)+1) * [0]

        for i in range(len(s)):

            if i > 0 and res[i] == 0:
                continue

            wd = wordDict

            d = 1


            while i + d <= len(s):
                check = s[i:i+d]
                wd = [word for word in wd if word.startswith(check)]

                if check in wd:

                    res[i+d] = 1
                
                d+=1
                
        return res[-1] == 1
                
                


