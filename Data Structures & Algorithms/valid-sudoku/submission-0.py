class Solution:

    def check_nums(self, arr):
        digs = [n for n in arr if n.isnumeric()]
        if len(digs) != len(set(digs)): 
            return True
        

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # box
        for r in range(3):
            for c in range(3):

                arr = ( board[r*3][c*3:c*3+3] + 
                        board[r*3+1][c*3:c*3+3] + 
                        board[r*3+2][c*3:c*3+3]
                )

                if self.check_nums(arr):
                    
                    return False        

        # diagonal

        for d in range(9):

            hor = board[d]

            ver = [board[i][d] for i in range(9)]

            if self.check_nums(hor) or self.check_nums(ver):
                return False
        
        return True


        