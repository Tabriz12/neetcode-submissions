class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        

        for r in range(1, len(matrix)):
            for c in range(len(matrix)):

                lc = float('inf') if c == 0 else matrix[r-1][c-1]
                m = matrix[r-1][c]
                rc = float('inf') if c == len(matrix)-1 else matrix[r-1][c+1]

                matrix[r][c] += min(lc,m,rc)
            
        

        return min(matrix[-1])


