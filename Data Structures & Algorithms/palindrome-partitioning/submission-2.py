class Solution:

    def __init__(self):

        self.res = []

    def isPal(self, st):

        return st == st[::-1]
    

    def slasher(self, s, path):

        '''
        l=0, r=1, s=aab
        l=0, r=1, s=ab
        l=0,r=1, s=b --- path
        l=0 r=2 s=ab ---nopal
        l=1,r=2 s=ab

        '''
        

        for r in range(1, len(s)+1):

            check = s[:r]

            if self.isPal(check):

                path.append(check)

                if r < len(s):
                    self.slasher(s[r:], path)
                
                else:
                    self.res.append(path[:])
                
                path.pop()
                        




    def partition(self, s: str):

        self.slasher(s, [])
        return self.res

        


                    
        
