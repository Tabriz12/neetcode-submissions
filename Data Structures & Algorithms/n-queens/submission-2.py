from collections import defaultdict
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        
        res = []

        cols = set()
        diag1 = set()
        diag2 = set()

        def backtrack(row, path):
            if row == n:
                res.append(path[:])
                return

            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue

                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                backtrack(row + 1, path + [col])

                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0, [])

        # build board
        final = []
        for way in res:
            board = []
            for c in way:
                row = ["." ] * n
                row[c] = "Q"
                board.append("".join(row))
            final.append(board)

        return final

            





        
        