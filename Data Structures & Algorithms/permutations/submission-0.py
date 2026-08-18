class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:



        res = []

        def backtrack(path, choices):


            if not choices:

                res.append(path)
                return
            

            for c in choices:

                
                
                diff = set(choices).difference(set([c]))

                backtrack(path+[c], list(diff))
        


        backtrack([], nums)

        return res
        