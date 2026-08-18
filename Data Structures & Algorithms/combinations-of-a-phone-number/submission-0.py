from collections import defaultdict
class Solution:

    def __init__(self):

        self.res = []

    def letterCombinations(self, digits: str) -> List[str]:

        start = 97
        lookup = defaultdict(list)
        for digit in range(2, 10):

            step = 4 if digit in [7, 9] else 3

            for _ in range(step):

                lookup[str(digit)].append(chr(start))
                start+=1
        

        def backtrack(path, idx):

            
            if idx == len(digits):
                if idx>0:
                    self.res.append(path)
                return
            

            for ltr in lookup[digits[idx]]:

                backtrack(path+ltr, idx+1)
        
        backtrack("", 0)
        return self.res
            







        

        