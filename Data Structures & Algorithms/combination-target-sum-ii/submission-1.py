class Solution:


    def __init__(self):

        self.res = []



    def backtrack(self, path, options, cursum, target):

        # [1,2,2,4,5,6,9]

        for idx, el in enumerate(options):

            if idx > 0 and el == options[idx-1]:
                continue

            if cursum + el < target:

                self.backtrack(path + [el], options[idx+1:], cursum + el, target)
            
            elif cursum + el == target:

                self.res.append(path+[el])




    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()

        self.backtrack([], candidates, 0, target)

        return self.res







        





        