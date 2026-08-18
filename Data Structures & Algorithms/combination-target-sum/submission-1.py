class Solution:

    def __init__(self):
        self.res = []


    def backtrack(self, path, options, target):
        
        for idx, el in enumerate(options):

            if sum(path) + el == target:
                self.res.append(path + [el])
            
            elif sum(path) + el < target:
                self.backtrack(path + [el], options[idx:], target)
            




    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:


        self.backtrack([], nums, target)
        return self.res






        
        