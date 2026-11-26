class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        switch = False

        if len(word1) > len(word2):

            switch = True
            word1, word2 = word2, word1


        

        res = ""

        for i in range(len(word1)):

            res += word2[i] + word1[i] if switch else word1[i] + word2[i]
        

        res += word2[len(word1):]

        return res
        





        