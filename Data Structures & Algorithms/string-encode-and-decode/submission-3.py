class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ""
        for s in strs:

            leng = len(s)

            pre = "0" * (3-len(str(leng))) + str(leng)

            res += pre + s
        
        return res




    def decode(self, s: str) -> List[str]:

        i = 0

        res = []
        while i < len(s):

            leng = int(s[i: i+3])

            i += 3

            word = s[i:i+leng] if leng else ""

            res.append(word)

            i+=leng
        
        return res







