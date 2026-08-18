class Solution:

    def __init__(self):

        self.cache = {1:1,
                    0:1}
    def climbStairs(self, n: int) -> int:
        
        if n not in self.cache:

            for i in range(len(self.cache), n+1):

                self.cache[i] = self.cache[i-1] + self.cache[i-2]
        
        return self.cache[n]
            
        


        