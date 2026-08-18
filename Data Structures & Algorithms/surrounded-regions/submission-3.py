from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:


        m = len(board)

        n = len(board[0])

        visited = set()

        q = deque()

        for r in range(m):
            for c in range(n):

                if board[r][c] == 'X' or (0 < r < m-1 and 0 < c < n-1):
                    continue
                

                q.append((r,c))
        

        dirs = [(0,1), (0,-1), (1,0), (-1, 0)]
        while q:

            print(q)
            for _ in range(len(q)):
                r,c = q.popleft()

                if (r,c) in visited:
                    continue
                
                visited.add((r,c))

                print(visited)

                for dx,dy in dirs:

                    x, y = r-dx, c-dy

                    #print(x,y)

                    if (x,y) in visited:
                        continue

                    if min(x,y)>=0 and x < m and y < n and board[x][y] == 'O':
                        #print(f"adding to queue, {x}, {y}")
                        q.append((x,y))
        

        for r in range(1, m-1):
            for c in range(1, n-1):

                if board[r][c] == "X":
                    continue
                
                else:
                    if (r,c) not in visited:
                        board[r][c] = "X"




            
            
        


                



            


            


                




                







        