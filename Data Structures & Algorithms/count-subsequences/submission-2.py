class Solution:

    def dp(self, s, t):


        ROWS, COLS = len(t)+1, len(s) + 1
        dp = [COLS * [0] for _ in range(ROWS)]

        '''
        cat

        caaat

        tacacaactaat

            x x y x y
        x   1 1 1 1 0
        y   1 1 2 2 1

            x y
        x   1 0
        x   2 0
        x   3 0
        y   0 3
        x   3 1
        y   3 4

            c a a a c
        c   1 1 1 1 1
        a   0 2 2  0
        c   0 0 0 0 5

            c a c
        c   3 3 2
        a   0 3 1
        a   0 2 1
        a   0 1 1
        c   0 0 1 

        '''

        for r in range(ROWS):

            dp[r][COLS-1] = 1

        for c in range(COLS-1, -1, -1):
            for r in range(ROWS-1, -1 ,-1):

                if t[r] == s[c]:
                    pass
                    #dp[r][c] = 
                
        

        print(dp)
        

        return dp[r][c]
    

    def rec(self, s, t):
        from functools import cache
        
        @cache
        def dfs(i, j):

            if j == len(t):

                return 1

            if len(t) - j > len(s) - i or i == len(s):
                return 0

            res = 0
            if s[i] == t[j]:

                res += dfs(i+1, j+1)
            
            res += dfs(i+1, j)

            return res
        
        return dfs(0,0)
            










    def numDistinct(self, s: str, t: str) -> int:

        return self.rec(s, t)
    


    
        















        