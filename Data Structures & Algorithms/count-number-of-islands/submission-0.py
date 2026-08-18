class Solution:


    def numIslands(self, grid: List[List[str]]) -> int:

        visited: set[tuple] = set()
        rows = len(grid)
        cols  = len(grid[0])
        islands = 0

        def dfs(r, c):

            if r == rows or c == cols or r < 0 or c < 0:
                return

            elif grid[r][c] == '0' or (r,c) in visited:
                return
            
            
                
            elif grid[r][c] == '1':

                visited.add((r,c))
                dfs(r, c+1)
                dfs(r+1,c)
                dfs(r, c-1)
                dfs(r-1, c)
                


        for r in range(rows):

            for c in range(cols):

                if grid[r][c] == '1' and (r,c) not in visited:
                    islands+=1
                    dfs(r, c)
        
        return islands
                











        