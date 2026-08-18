class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        '''
        r0 c0:max -> cMax-r1:rmax -> rmax: c max-1:0, rmax-1



        



        '''

        res = []

        rows = len(matrix)
        cols = len(matrix[0])

        rs = 0
        cs = 0

        while rs < rows and cs < cols:

            for c in range(cs, cols):

                res.append(matrix[rs][c])
            
            rs +=1

            for r in range(rs, rows):

                res.append(matrix[r][cols-1])
            
            cols -=1

            if not (rs < rows and cs < cols):
                break

            for c in range(cols-1, cs-1, -1):

                res.append(matrix[rows-1][c])
            
            rows -=1

            for r in range(rows-1, rs-1, -1):

                res.append(matrix[r][cs])
            
            cs+=1

            
        
        return res

        