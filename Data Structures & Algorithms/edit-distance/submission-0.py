class Solution:
    def minDistance(self, word1: str, word2: str) -> int:


        m = [(len(word1) +1) * [0] for _ in range(len(word2)+1)]

        """

        moooonkeys


        0 0 0 0 0 0 0 0 0 0
        0 0 0 0 0 0 0 0 0 0
        0 0 0 0 0 0 0 0 0 0
        0 0 0 0 0 0 0 0 0 0
        0 0 0 0 0 0 0 0 0 0
        0 0 0 0 0 0 0 0 0 0




        money
        """

        for j in range(len(word1), -1, -1):

            m[len(word2)][j] = len(word1) - j
        
        for i in range(len(word2), -1 , -1):

            m[i][len(word1)] = len(word2) - i

            

        for j in range(len(word1)-1,-1,-1):

            for i in range(len(word2)-1,-1,-1):

                if word1[j] == word2[i]:

                    m[i][j] = m[i+1][j+1]
                
                else:

                    m[i][j] = 1 + min(m[i+1][j], m[i][j+1], m[i+1][j+1])
                
        return m[0][0]
        






        