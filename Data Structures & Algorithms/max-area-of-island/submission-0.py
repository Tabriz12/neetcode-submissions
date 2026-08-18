class Solution:
    def __init__(self):

        self.stk = 0
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        res = 0


        def dfs(grid, r, c):

            if r < 0 or c < 0 or r==rows or c == cols:
                return
            
            if grid[r][c] == 0:
                return
            
            else:

                self.stk+=1
                grid[r][c] = 0

                dfs(grid, r, c+1)
                dfs(grid, r+1, c)
                dfs(grid, r, c-1)
                dfs(grid, r-1, c)
        

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == 1:

                    dfs(grid, r, c)
                
                    res = max(res, self.stk)

                    self.stk = 0
        
        return res


                

         
        