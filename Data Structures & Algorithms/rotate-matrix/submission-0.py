class Solution:


    def transpose(self, matrix):


        rows = len(matrix)

        for r in range(rows):
            for c in range(r+1, rows):

                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        
        return matrix

    def rotate(self, matrix: List[List[int]]) -> None:


        matrix = self.transpose(matrix)

        matrix = [r.reverse() for r in matrix]


        


