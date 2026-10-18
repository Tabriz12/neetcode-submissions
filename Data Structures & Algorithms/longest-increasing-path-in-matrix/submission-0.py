class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:


        ROWS = len(matrix)
        COLS = len(matrix[0])

        dp = [[0] * COLS for _ in range(ROWS)]

        self.mas = 0
        
        def dfs(r, c, preVal):

            

            if r < 0 or c < 0 or r >= ROWS or c >= COLS:

                return 0

            curVal = matrix[r][c]

            if preVal >= curVal:
                return 0
                        
            if dp[r][c] > 0:

                return dp[r][c]
            
            left = dfs(r, c-1, curVal)
            right = dfs(r, c+1, curVal)
            up = dfs(r-1, c, curVal)
            down = dfs(r+1, c, curVal)

            res = max(left, right, up, down) + 1

            self.mas = max(res, self.mas)

            dp[r][c] = res

            return res
        

        for r in range(ROWS):
            for c in range(COLS):

                dfs(r, c, -1)

        print(dp)

        return self.mas


        

        