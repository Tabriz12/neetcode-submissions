import numpy as np

class DSU:

    def __init__(self, n):

        self.heads = [i for i in range(n)]
        self.lens = [1] * n

    
    def find(self, n):

        if self.heads[n] != n:

            self.heads[n] = self.find(self.heads[n])
        
        return self.heads[n]
    

    def union(self, u, v):

        hv = self.find(v)

        hu = self.find(u)


        if hv == hu:
            return False
        

        if self.lens[hv] < self.lens[hu]:
            hv, hu = hu, hv

        
        self.lens[hv] += self.lens[hu]
        self.heads[hu] = hv




class Solution:

    
    def swimInWater(self, grid: List[List[int]]) -> int:


        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        N = len(grid)

        dsu = DSU(N*N)
        nodes = []

        for r in range(N):
            for c in range(N):

                nodes.append([grid[r][c], r, c])
        
        nodes.sort(key=lambda x: x[0])



        for t,r,c in nodes:

            for dx, dy in dirs:

                nr, nc = r+dx, c+dy

                if 0 <= nr < N and 0 <=nc< N and t > grid[nr][nc]:

                    dsu.union(N*r+c, N*nr + nc)
                

            if dsu.find(0) == dsu.find(N*N-1):
                return t









        






        